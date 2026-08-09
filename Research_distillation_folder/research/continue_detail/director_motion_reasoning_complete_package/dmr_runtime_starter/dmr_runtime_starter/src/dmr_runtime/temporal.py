from __future__ import annotations

from dataclasses import dataclass
from math import inf, isinf
from typing import Iterable

from .models import TemporalConstraint


@dataclass(frozen=True)
class DifferenceEdge:
    source: str
    target: str
    weight: float
    constraint_id: str
    explanation: str | None


@dataclass(frozen=True)
class TemporalConflict:
    points: list[str]
    constraint_ids: list[str]
    message: str


@dataclass(frozen=True)
class TemporalSolution:
    consistent: bool
    schedule_s: dict[str, float]
    earliest_s: dict[str, float | None]
    latest_s: dict[str, float | None]
    underconstrained_points: list[str]
    conflict: TemporalConflict | None = None


class STNSolver:
    """Simple Temporal Network solver for constraints l <= right-left <= u.

    The implementation is deterministic and self-contained. It uses Bellman-Ford
    to find a feasible potential and a negative-cycle explanation, then
    Floyd-Warshall to compute all-pairs implied upper bounds.
    """

    SUPER = "__stn_super_source__"

    def __init__(self, constraints: Iterable[TemporalConstraint], *, origin: str = "scene:start") -> None:
        self.constraints = list(constraints)
        self.origin = origin
        self.points = {origin}
        self.edges: list[DifferenceEdge] = []
        for c in self.constraints:
            self.points.update((c.left_point, c.right_point))
            # right - left <= max  => right <= left + max
            self.edges.append(DifferenceEdge(c.left_point, c.right_point, c.max_delta_s, c.constraint_id, c.explanation))
            # right - left >= min  => left <= right - min
            self.edges.append(DifferenceEdge(c.right_point, c.left_point, -c.min_delta_s, c.constraint_id, c.explanation))

    def solve(self) -> TemporalSolution:
        conflict, potentials = self._bellman_ford()
        if conflict:
            return TemporalSolution(False, {}, {}, {}, [], conflict)
        distances = self._all_pairs_upper_bounds()
        origin = self.origin
        schedule = {point: potentials[point] - potentials[origin] for point in sorted(self.points)}
        earliest: dict[str, float | None] = {}
        latest: dict[str, float | None] = {}
        under: list[str] = []
        for point in sorted(self.points):
            upper = distances[origin][point]
            reverse = distances[point][origin]
            latest[point] = None if isinf(upper) else upper
            earliest[point] = None if isinf(reverse) else -reverse
            if point != origin and (isinf(upper) or isinf(reverse)):
                under.append(point)
        return TemporalSolution(True, schedule, earliest, latest, under, None)

    def _bellman_ford(self) -> tuple[TemporalConflict | None, dict[str, float]]:
        points = sorted(self.points)
        all_edges = list(self.edges) + [DifferenceEdge(self.SUPER, p, 0.0, "__super__", None) for p in points]
        dist = {p: 0.0 for p in points}
        dist[self.SUPER] = 0.0
        pred: dict[str, DifferenceEdge] = {}
        updated: str | None = None
        for _ in range(len(points) + 1):
            updated = None
            for edge in all_edges:
                if dist[edge.target] > dist[edge.source] + edge.weight + 1e-12:
                    dist[edge.target] = dist[edge.source] + edge.weight
                    pred[edge.target] = edge
                    updated = edge.target
            if updated is None:
                break
        if updated is None:
            return None, {p: dist[p] for p in points}

        cycle_node = updated
        for _ in range(len(points) + 1):
            edge = pred.get(cycle_node)
            if edge is None:
                break
            cycle_node = edge.source

        cycle_edges: list[DifferenceEdge] = []
        seen: dict[str, int] = {}
        current = cycle_node
        while current not in seen and current in pred:
            seen[current] = len(cycle_edges)
            edge = pred[current]
            cycle_edges.append(edge)
            current = edge.source
        if current in seen:
            cycle_edges = cycle_edges[seen[current]:]
        cycle_edges.reverse()
        ids = [e.constraint_id for e in cycle_edges if e.constraint_id != "__super__"]
        points_in_cycle = [e.source for e in cycle_edges]
        if cycle_edges:
            points_in_cycle.append(cycle_edges[-1].target)
        ids = list(dict.fromkeys(ids))
        msg = "Inconsistent temporal constraints form a negative cycle"
        if ids:
            msg += ": " + ", ".join(ids)
        return TemporalConflict(points_in_cycle, ids, msg), {}

    def _all_pairs_upper_bounds(self) -> dict[str, dict[str, float]]:
        pts = sorted(self.points)
        d = {i: {j: (0.0 if i == j else inf) for j in pts} for i in pts}
        for edge in self.edges:
            if edge.weight < d[edge.source][edge.target]:
                d[edge.source][edge.target] = edge.weight
        for k in pts:
            for i in pts:
                if isinf(d[i][k]):
                    continue
                for j in pts:
                    via = d[i][k] + d[k][j]
                    if via < d[i][j]:
                        d[i][j] = via
        return d
