# heuristic.py
# Heuristic function for A* search


def heuristic(state):
    """
    Admissible heuristic for the bridge and torch puzzle:
    - If everyone already crossed: 0
    - If the torch is on the left: use the slowest on the left
    - If the torch is on the right: fastest on the right + slowest on the left
    """
    left, right, torch = state
    if not left:
        return 0
    slowest_left = max(left)
    if torch == 0:
        return slowest_left
    if right:
        return min(right) + slowest_left
    return slowest_left
