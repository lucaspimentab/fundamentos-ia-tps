from utils import get_possible_states, freeze
from heuristic import heuristic
import time
import heapq

# a_star search implementation

def a_star(start_state, goal_check):
    pq = [(heuristic(start_state), 0, start_state, [start_state])]
    g_cost = {freeze(start_state): 0}
    expanded = 0
    t0 = time.perf_counter()
    visited = set()

    while pq:
        f, cost, state, path = heapq.heappop(pq)
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
                "method": "A*",
            }

        next_states, costs = get_possible_states(state)
        for ns, c in zip(next_states, costs):
            new_g = cost + c
            frozen_ns = freeze(ns)
            if frozen_ns not in g_cost or new_g < g_cost[frozen_ns]:
                g_cost[frozen_ns] = new_g
                f_new = new_g + heuristic(ns)
                heapq.heappush(pq, (f_new, new_g, ns, path + [ns]))

    return {"found": False, "expanded": expanded, "time": time.perf_counter() - t0, "method": "A*"}


# ===========================================================
# A* search implementation      