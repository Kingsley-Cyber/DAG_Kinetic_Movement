<#
 =============================================================================
 cpcs_ontology_check.ps1
 Validates every .md file under cpcs/ against the controlled vocabulary and
 schema defined in cpcs/00_governance/policies/control_plane_reference.md.

 Usage:  pwsh -NoProfile -File .\cpcs_ontology_check.ps1
 Exit:   0 = clean, 1 = deviations found
 =============================================================================
#>
param(
    [string]$Root = (Join-Path $PSScriptRoot 'cpcs')
)

$ErrorActionPreference = 'Stop'

if (-not (Test-Path -LiteralPath $Root)) {
    throw "Root not found: $Root"
}

# ---------------------------------------------------------------------------
# Controlled vocabularies (must match control_plane_reference.md §6)
# ---------------------------------------------------------------------------

$ValidKinds = @(
    'agent_log', 'catalog', 'contract', 'doctrine', 'experiment_design',
    'fixture_set', 'gap_register', 'mechanism', 'method', 'metric_contract',
    'policy', 'principle', 'provider_finding', 'schema_draft', 'vocabulary'
) | ForEach-Object { $_ }  # force array even if single element

$ValidEpistemicStatuses = @(
    'SOURCE_EVIDENCE', 'INFERENCE', 'CREATIVE_CHOICE', 'PROJECT_DERIVED',
    'PROVIDER_EXPERIMENT', 'UNVERIFIED', 'CONTRADICTED', 'UNKNOWN'
)

$ValidAcquisitions = @(
    'authored', 'observed', 'detected', 'measured', 'estimated',
    'inferred', 'derived', 'interpreted', 'simulated', 'creative_choice'
)

$RequiredFields = @(
    'id', 'kind', 'epistemic_status', 'acquisition', 'sources', 'primary_route'
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

function Parse-Frontmatter {
    param([string]$Content)
    if ($Content -notmatch '(?s)^---\s*\r?\n(.*?)\r?\n---\s*\r?\n') {
        return $null
    }
    return $Matches[1]
}

function Get-Field {
    param([string]$Frontmatter, [string]$FieldName)
    # Match `field: value` or `field: [value]` on a single line
    if ($Frontmatter -match "(?m)^\s*$FieldName\s*:\s*(.+?)\s*$") {
        return $Matches[1].Trim()
    }
    return $null
}

function Get-Field-List {
    param([string]$Frontmatter, [string]$FieldName)
    # Match `field: [a, b, c]` or `field: []`
    if ($Frontmatter -match "(?m)^\s*$FieldName\s*:\s*\[(.*)\]\s*$") {
        $raw = $Matches[1].Trim()
        if ($raw -eq '') { return @() }
        return ($raw -split ',') | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne '' }
    }
    return $null  # might be multi-line list — caller checks
}

function Get-Field-Multiline {
    param([string]$Frontmatter, [string]$FieldName)
    # Match `field:` followed by indented list items on subsequent lines
    $pattern = "(?ms)^\s*$FieldName\s*:\s*\r?\n((?:\s+-\s+.+\r?\n)+)"
    if ($Frontmatter -match $pattern) {
        $block = $Matches[1]
        $items = @()
        foreach ($line in ($block -split "`n")) {
            if ($line -match '^\s+-\s+(.+)') {
                $items += $Matches[1].Trim()
            }
        }
        return $items
    }
    return $null
}

# ---------------------------------------------------------------------------
# Scan
# ---------------------------------------------------------------------------

$files = Get-ChildItem -Path $Root -Recurse -Filter *.md
$allIds = @{}
$deviations = @()
$fileCount = 0
$checkedCount = 0

foreach ($f in $files) {
    $fileCount++
    $relPath = $f.FullName.Substring((Get-Location).Path.Length).TrimStart('\', '/')
    $content = Get-Content $f.FullName -Raw -ErrorAction SilentlyContinue

    if (-not $content) {
        $deviations += "[EMPTY FILE] $relPath — file is empty or unreadable"
        continue
    }

    $fm = Parse-Frontmatter -Content $content
    if (-not $fm) {
        $deviations += "[NO FRONTMATTER] $relPath — missing YAML frontmatter block"
        continue
    }

    $checkedCount++

    # --- Classify file type by path ---
    $normPath = $relPath -replace '\\', '/'
    $isLedger = $normPath -match '/research/distillation/ledger/'
    $isRegistration = $normPath -match '/research/source_registry/identities/'

    if ($isLedger) {
        # --- Ledger schema ---
        $ledgerId = Get-Field -Frontmatter $fm -FieldName 'distillation_id'
        $sourceId = Get-Field -Frontmatter $fm -FieldName 'source_id'
        $status = Get-Field -Frontmatter $fm -FieldName 'status'
        $coverage = Get-Field -Frontmatter $fm -FieldName 'coverage'

        foreach ($field in @('distillation_id', 'source_id', 'status', 'coverage')) {
            $value = Get-Field -Frontmatter $fm -FieldName $field
            if (-not $value) {
                $deviations += "[MISSING FIELD] $relPath — ledger field '$field' is absent or empty"
            }
        }

        if ($ledgerId) {
            if ($ledgerId -notmatch '^DIST-\d{3}$') {
                $deviations += "[INVALID LEDGER ID] $relPath — distillation_id '$ledgerId' does not match DIST-NNN"
            }
            if ($allIds.ContainsKey($ledgerId)) {
                $deviations += "[DUPLICATE ID] $relPath — distillation_id '$ledgerId' already used by $($allIds[$ledgerId])"
            } else {
                $allIds[$ledgerId] = $relPath
            }
        }
        continue
    }

    if ($isRegistration) {
        # --- Registration schema ---
        $regId = Get-Field -Frontmatter $fm -FieldName 'id'
        $regTitle = Get-Field -Frontmatter $fm -FieldName 'title'
        $regVersion = Get-Field -Frontmatter $fm -FieldName 'version'
        $regEpistemic = Get-Field -Frontmatter $fm -FieldName 'epistemic_class'

        foreach ($field in @('id', 'title', 'version', 'epistemic_class')) {
            $value = Get-Field -Frontmatter $fm -FieldName $field
            if (-not $value) {
                $deviations += "[MISSING FIELD] $relPath — registration field '$field' is absent or empty"
            }
        }

        if ($regId) {
            if ($regId -notmatch '^SRC-\d{3}$') {
                $deviations += "[INVALID REGISTRATION ID] $relPath — id '$regId' does not match SRC-NNN"
            }
            if ($allIds.ContainsKey($regId)) {
                $deviations += "[DUPLICATE ID] $relPath — id '$regId' already used by $($allIds[$regId])"
            } else {
                $allIds[$regId] = $relPath
            }
        }
        continue
    }

    # --- Knowledge-card schema (default) ---
    $cardId = Get-Field -Frontmatter $fm -FieldName 'id'
    $kind = Get-Field -Frontmatter $fm -FieldName 'kind'
    $epistemicStatus = Get-Field -Frontmatter $fm -FieldName 'epistemic_status'
    $acquisition = Get-Field -Frontmatter $fm -FieldName 'acquisition'
    $sources = Get-Field -Frontmatter $fm -FieldName 'sources'
    $primaryRoute = Get-Field -Frontmatter $fm -FieldName 'primary_route'

    # --- Check required fields ---
    foreach ($field in $RequiredFields) {
        $value = Get-Field -Frontmatter $fm -FieldName $field
        if (-not $value) {
            $deviations += "[MISSING FIELD] $relPath — required field '$field' is absent or empty"
        }
    }

    # --- Check id format ---
    if ($cardId) {
        if ($cardId -match '^cpcs\.' -or $cardId -match '^SRC-\d{3}$' -or $cardId -match '^DIST-\d{3}$') {
            # valid pattern
        } else {
            $deviations += "[INVALID ID FORMAT] $relPath — id '$cardId' does not match cpcs.* / SRC-NNN / DIST-NNN"
        }

        # --- Check id uniqueness ---
        if ($allIds.ContainsKey($cardId)) {
            $deviations += "[DUPLICATE ID] $relPath — id '$cardId' already used by $($allIds[$cardId])"
        } else {
            $allIds[$cardId] = $relPath
        }

        # --- Check id leaf is snake_case (for cpcs.* ids) ---
        if ($cardId -match '^cpcs\.') {
            $leaf = $cardId.Split('.')[-1]
            if ($leaf -notmatch '^[a-z][a-z0-9_]*$') {
                $deviations += "[INVALID ID LEAF] $relPath — id leaf '$leaf' is not snake_case"
            }
        }
    }

    # --- Check kind ---
    if ($kind) {
        $kind = $kind.Trim('"').Trim("'")
        if ($kind -notin $ValidKinds) {
            $deviations += "[INVALID KIND] $relPath — kind '$kind' not in controlled vocabulary: $($ValidKinds -join ', ')"
        }
    }

    # --- Check epistemic_status ---
    if ($epistemicStatus) {
        $epistemicStatus = $epistemicStatus.Trim('"').Trim("'")
        if ($epistemicStatus -notin $ValidEpistemicStatuses) {
            $deviations += "[INVALID EPISTEMIC_STATUS] $relPath — epistemic_status '$epistemicStatus' not in: $($ValidEpistemicStatuses -join ', ')"
        }
    }

    # --- Check acquisition ---
    if ($acquisition) {
        $acquisition = $acquisition.Trim('"').Trim("'")
        if ($acquisition -notin $ValidAcquisitions) {
            $deviations += "[INVALID ACQUISITION] $relPath — acquisition '$acquisition' not in: $($ValidAcquisitions -join ', ')"
        }
    }

    # --- Check sources is non-empty (for knowledge cards) ---
    if ($cardId -and $cardId -match '^cpcs\.') {
        if ($sources -eq '[]' -or -not $sources) {
            $deviations += "[EMPTY SOURCES] $relPath — knowledge card has no source references"
        }
    }

    # --- Check primary_route matches actual file location ---
    if ($primaryRoute) {
        $primaryRoute = $primaryRoute.TrimEnd('/')
        $fileDir = $f.DirectoryName -replace '\\', '/'
        $expectedBase = (Get-Location).Path -replace '\\', '/'
        if (-not $fileDir.EndsWith($primaryRoute)) {
            $deviations += "[ROUTE MISMATCH] $relPath — primary_route '$primaryRoute' does not match file directory '$($f.DirectoryName)'"
        }
    }
}

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

Write-Host ""
Write-Host "=== CPCS Ontology Check ===" -ForegroundColor Cyan
Write-Host "Files scanned:      $fileCount"
Write-Host "Files with FM:      $checkedCount"
Write-Host "Unique IDs found:   $($allIds.Count)"
Write-Host "Deviations found:   $($deviations.Count)"
Write-Host ""

if ($deviations.Count -eq 0) {
    Write-Host "RESULT: CLEAN — all files conform to the control plane reference." -ForegroundColor Green
    Write-Host ""
    exit 0
} else {
    Write-Host "RESULT: DEVIATIONS DETECTED" -ForegroundColor Red
    Write-Host ""
    Write-Host "--- Deviation list ---" -ForegroundColor Yellow
    foreach ($d in $deviations) {
        Write-Host "  $d" -ForegroundColor Red
    }
    Write-Host ""
    Write-Host "Fix all deviations before proceeding with distillation." -ForegroundColor Yellow
    Write-Host ""
    exit 1
}
