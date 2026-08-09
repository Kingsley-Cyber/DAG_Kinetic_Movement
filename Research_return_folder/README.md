# Research Return Folder

> **Intake point for the research-return loop (automation doctrine D9).**
> The user performs deep research on an open gap (see
> `cpcs/research/gaps/understanding_gap_register.md`, UG ids) and returns it
> here — or directly in chat — for ingestion into the knowledge tree.

## How to use

1. Open a gap in the understanding register (UG-NNN) and do the deep research.
2. Drop your findings here: any format (markdown, PDF, notes, URLs, raw text,
   JSONL). Name the file with the gap id when possible, e.g.
   `UG-002_rhythm_vs_phase_reconciliation.md`.
3. Tell the agent which UG id(s) the research targets (or the agent will
   match it).
4. The agent ingests it like a source (REUSE/EXTEND/SUPPORT/CREATE per
   doctrine D2), updates the gap status (RESEARCHING → RETURNED → CLOSED or
   REFINED) with an evidence link and closure note, then runs housekeeping
   H1–H7 and appends a working-agent-log entry (H6).

## Rules of the loop

- Research that only restates existing tree content is SUPPORT, not new
  evidence — the gap stays open.
- Partial resolution → gap REFINED (re-scoped, children re-targeted); never
  closed by assumption (doctrine D6).
- Contradictions with existing claims go to PASS 7 and the contradictions
  register before any status change.
- Every ingestion is recorded: gap register update + agent log entry +
  outstanding_actions sync.
