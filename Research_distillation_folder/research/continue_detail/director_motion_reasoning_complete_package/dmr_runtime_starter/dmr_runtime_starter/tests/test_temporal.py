from dmr_runtime.models import TemporalConstraint
from dmr_runtime.temporal import STNSolver


def c(cid, left, right, lo, hi):
    return TemporalConstraint(
        constraint_id=cid,
        left_point=left,
        right_point=right,
        min_delta_s=lo,
        max_delta_s=hi,
    )


def test_stn_solves_exact_and_bounded_times():
    solution = STNSolver([
        c("a", "zero", "attack:start", 1.0, 1.0),
        c("b", "attack:start", "contact", 0.4, 0.6),
        c("c", "contact", "reaction", 0.0, 0.2),
        c("d", "zero", "reaction", 1.5, 1.7),
    ], origin="zero").solve()
    assert solution.consistent
    assert solution.earliest_s["attack:start"] == 1.0
    assert solution.latest_s["attack:start"] == 1.0
    assert 1.5 - 1e-9 <= solution.schedule_s["reaction"] <= 1.7 + 1e-9
    assert not solution.underconstrained_points


def test_stn_reports_negative_cycle_and_constraint_ids():
    solution = STNSolver([
        c("a_before_b", "a", "b", 1.0, 2.0),
        c("b_before_a", "b", "a", 1.0, 2.0),
    ], origin="a").solve()
    assert not solution.consistent
    assert solution.conflict is not None
    assert set(solution.conflict.constraint_ids) == {"a_before_b", "b_before_a"}


def test_stn_marks_disconnected_point_underconstrained():
    solution = STNSolver([
        c("duration", "zero", "end", 4.0, 4.0),
        c("floating_relation", "x", "y", 0.5, 1.0),
    ], origin="zero").solve()
    assert solution.consistent
    assert {"x", "y"}.issubset(set(solution.underconstrained_points))
