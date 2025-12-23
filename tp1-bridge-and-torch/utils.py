# utils.py
import copy
from itertools import combinations

# State: ([left_side], [right_side], torch_side)
# torch_side = 0 -> torch on the left
# torch_side = 1 -> torch on the right


def get_possible_states(state):
    """
    Return (next_states, costs) from the given state.
    Each successor moves 1 or 2 people from the side with the torch.
    Cost = time of the slowest traveler in the chosen group.
    """
    torch_side = state[2]
    current_side = state[torch_side]

    choices = []
    for i in [1, 2]:
        choices += list(combinations(current_side, i))

    next_states = []
    costs = []

    for possible in choices:
        new_state = copy.deepcopy(state)
        new_state[torch_side] = list(set(new_state[torch_side]) - set(possible))
        new_state[not torch_side] += list(possible[:])
        new_state[2] = not torch_side
        cost = max(possible)
        next_states.append(new_state)
        costs.append(cost)

    return next_states, costs


def goal_check(state):
    """Goal: left side empty and torch on the right."""
    return len(state[0]) == 0 and state[2] == 1


def freeze(state):
    """Convert lists to immutable tuples so they can be hashed."""
    return (tuple(sorted(state[0])), tuple(sorted(state[1])), state[2])


def print_solution(result):
    if not result["found"]:
        print(f"{result['method']}: Nenhuma solucao encontrada.")
        return
    print(f"\n=== {result['method']} ===")
    print(
        f"Custo total: {result['cost']} min | Nos expandidos: {result['expanded']} | Tempo: {result['time']*1000:.2f} ms"
    )
    for i, state in enumerate(result["path"]):
        left, right, torch = state
        print(f"Estado {i:02d}: L={left} | R={right} | T={'L' if torch == 0 else 'R'}")
