# depth-first search (DFS) implementation
from utils import get_possible_states, freeze
import time


def dfs(start_state, goal_check):
    stack = [(start_state, [start_state], 0)]
    visited = set()
    expanded = 0
    t0 = time.perf_counter()

    while stack:
        state, path, cost = stack.pop()

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
                "method": "DFS",
            }

        next_states, costs = get_possible_states(state)
        for ns, c in zip(next_states, costs):
            stack.append((ns, path + [ns], cost + c))

    return {"found": False, "expanded": expanded, "time": time.perf_counter() - t0, "method": "DFS"}
# depth-first search (DFS) implementation