# breadth-first search (BFS) implementation
from utils import get_possible_states, freeze
import time
from collections import deque

def bfs(start_state, goal_check):
    queue = deque([(start_state, [start_state], 0)])
    visited = {freeze(start_state)}
    expanded = 0
    t0 = time.perf_counter()

    while queue:
        state, path, cost = queue.popleft()
        expanded += 1

        if goal_check(state):
            return {
                "found": True,
                "path": path,
                "cost": cost,
                "expanded": expanded,
                "time": time.perf_counter() - t0,
                "method": "BFS",
            }

        next_states, costs = get_possible_states(state)
        for ns, c in zip(next_states, costs):
            frozen = freeze(ns)
            if frozen not in visited:
                visited.add(frozen)
                queue.append((ns, path + [ns], cost + c))

    return {"found": False, "expanded": expanded, "time": time.perf_counter() - t0, "method": "BFS"}