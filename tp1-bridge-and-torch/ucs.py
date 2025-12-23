# ucs.py
# uniform-cost search (UCS) implementation

from utils import get_possible_states, freeze
import time
import heapq

def ucs(start_state, goal_check):
    pq = [(0, start_state, [start_state])]
    visited = set()
    expanded = 0
    t0 = time.perf_counter()

    while pq:
        cost, state, path = heapq.heappop(pq)
        frozen = freeze(state)
        if frozen in visited:
            continue
        visited.add(frozen)
        expanded += 1

        if goal_check(state):
            return {
                "found": True,
                "path": path,
                "cost": cost,
                "expanded": expanded,
                "time": time.perf_counter() - t0,
                "method": "UCS",
            }

        next_states, costs = get_possible_states(state)
        for ns, c in zip(next_states, costs):
            heapq.heappush(pq, (cost + c, ns, path + [ns]))

    return {"found": False, "expanded": expanded, "time": time.perf_counter() - t0, "method": "UCS"}
# uniform-cost search (UCS) implementation