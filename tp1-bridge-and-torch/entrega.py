import copy
from bfs import bfs
from dfs import dfs
from ucs import ucs
from a_star import a_star
from utils import print_solution, goal_check

"""
State format: ([left_side], [right_side], torch_side)
- torch_side: 0 -> torch on the left; 1 -> torch on the right.
Start state: ([1, 2, 5, 10], [], 0)
Goal state: ([], [1, 2, 5, 10], 1)
Successors move 1 or 2 people from the torch side; edge cost = slowest traveler.
The search space is an implicit directed weighted graph generated on demand.
"""


def compare_all():
    start = [[1, 2, 5, 10], [], 0]
    algs = [dfs, bfs, ucs, a_star]
    for func in algs:
        result = func(copy.deepcopy(start), goal_check)
        print_solution(result)


if __name__ == "__main__":
    compare_all()
