from itertools import cycle
from math import lcm

Node = tuple[str, str]


def get_input(puzzle_input: list[str] = None) -> list[str]:
    """
    Read the input file and return a list of strings.
    Each string represents a line in the input file.
    """
    if puzzle_input:
        return puzzle_input

    with open("day_8/input/input.txt", "r") as f:
        return f.read().splitlines()


def process_input(puzzle_input: list[str]) -> dict[str, Node]:
    path = puzzle_input[0]

    nodes = {}
    for line in puzzle_input[2:]:
        node_name, left, right = line[:3], line[7:10], line[12:15]
        nodes[node_name] = {"L": left, "R": right}

    return path, nodes


def walk_to_node_zzz(path: str, nodes: dict[str, Node]) -> int:
    score = 0
    current_node = "AAA"
    cycler = cycle(path)

    while current_node != "ZZZ":
        current_node = nodes[current_node][next(cycler)]
        score += 1

    return score


def find_loop_length(path, nodes, start):
    """
    Walk through the graph twice, once with a step size of 1 and once with a step size of 2.
    When the two nodes are the same AND they're at the same step in the path, we've found a loop.
    """
    node_one = node_two = start

    first_cycler = cycle(path)
    second_cycler = cycle(path)

    i = 1
    while True:
        node_one = nodes[node_one][next(first_cycler)]
        node_two = nodes[node_two][next(second_cycler)]
        node_two = nodes[node_two][next(second_cycler)]

        if node_one == node_two and i % len(path) == (i * 2) % len(path):
            return i
        i += 1


def walk_all_to_z_nodes(path: str, nodes: dict[str, Node]) -> int:
    """
    Every loop ends with a Z node. Find the length of each loop and calculate the LCM. At that
    point, every ghost will be at a Z node.
    """
    start_nodes = [node for node in nodes if node[2] == "A"]
    loop_lengths = [find_loop_length(path, nodes, start) for start in start_nodes]
    lcm_loop_lengths = lcm(*loop_lengths)
    return lcm_loop_lengths


def solve_puzzle_1(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 1.
    """
    puzzle_input = get_input(puzzle_input)
    path, nodes = process_input(puzzle_input)

    score = walk_to_node_zzz(path, nodes)

    return score


def solve_puzzle_2(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 2.
    """
    puzzle_input = get_input(puzzle_input)
    path, nodes = process_input(puzzle_input)
    score = walk_all_to_z_nodes(path, nodes)

    return score


if __name__ == "__main__":
    solution_1 = solve_puzzle_1()
    print(f"The solution for puzzle 1 is: {solution_1}")

    solution_2 = solve_puzzle_2()
    print(f"The solution for puzzle 2 is: {solution_2}")
