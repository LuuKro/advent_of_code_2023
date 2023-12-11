from collections import defaultdict


class Pipe:
    def __init__(self):
        self.char = "."
        self.first = None
        self.second = None
        self.in_loop = False


def get_input(puzzle_input: list[str] = None) -> list[str]:
    """
    Read the input file and return a list of strings.
    Each string represents a line in the input file.
    """
    if puzzle_input:
        return puzzle_input

    with open("day_10/input/input.txt", "r") as f:
        return f.read().splitlines()


Map = defaultdict[defaultdict[Pipe]]


def process_input(puzzle_input: list[str]) -> tuple[tuple[int, int], Map]:
    """
    Process the input file and return the location of 'S' and a map of pipes.
    """
    pipe_dirs = {
        "|": ((0, -1), (0, 1)),
        "-": ((-1, 0), (1, 0)),
        "L": ((0, -1), (1, 0)),
        "J": ((-1, 0), (0, -1)),
        "7": ((-1, 0), (0, 1)),
        "F": ((1, 0), (0, 1)),
        ".": ((0, 0), (0, 0)),
        "S": ((0, 0), (0, 0)),
    }

    puzzle_map = defaultdict(lambda: defaultdict(Pipe))

    puzzle_map["y"] = len(puzzle_input)
    for y, line in enumerate(puzzle_input):
        puzzle_map["x"] = len(line)
        for x, char in enumerate(line):
            pipe = puzzle_map[x][y]
            pipe.x, pipe.y, pipe.char = x, y, char

            if char == "S":
                s_pipe = pipe
                s_x, s_y = x, y
                continue

            pipe_dir = pipe_dirs[char]
            puzzle_map[x][y].first = puzzle_map[x + pipe_dir[0][0]][y + pipe_dir[0][1]]
            puzzle_map[x][y].second = puzzle_map[x + pipe_dir[1][0]][y + pipe_dir[1][1]]

    s_connections = []
    to_left = to_right = to_up = False

    left_pipe = puzzle_map[s_x - 1][s_y]
    if left_pipe.first == puzzle_map[s_x][s_y] or left_pipe.second == puzzle_map[s_x][s_y]:
        to_left = True
        s_connections.append(left_pipe)

    right_pipe = puzzle_map[s_x + 1][s_y]
    if right_pipe.first is puzzle_map[s_x][s_y] or right_pipe.second is puzzle_map[s_x][s_y]:
        to_right = True
        s_connections.append(right_pipe)

    top_pipe = puzzle_map[s_x][s_y - 1]
    if top_pipe.first is puzzle_map[s_x][s_y] or top_pipe.second is puzzle_map[s_x][s_y]:
        to_up = True
        s_connections.append(top_pipe)

    bottom_pipe = puzzle_map[s_x][s_y + 1]
    if bottom_pipe.first is puzzle_map[s_x][s_y] or bottom_pipe.second is puzzle_map[s_x][s_y]:
        s_connections.append(bottom_pipe)

    if to_left:
        s_pipe.char = "-" if to_right else "J" if to_up else "F"
    elif to_right:
        s_pipe.char = "L" if to_up else "7"
    else:
        s_pipe.char = "|"

    s_pipe.first = s_connections[0]
    s_pipe.second = s_connections[1]

    return (s_x, s_y), puzzle_map


def walk_path(puzzle_map: Map, start_pos: tuple[int, int]) -> int:
    """
    Walk the path and mark all pipes that are part of the loop. Return the path length."""
    current_pipe = start_pipe = puzzle_map[start_pos[0]][start_pos[1]]
    next_pipe = current_pipe.first
    path_length = 1
    current_pipe.in_loop = True
    next_pipe.in_loop = True

    while next_pipe is not start_pipe:
        if current_pipe is next_pipe.first:
            temp_pipe = next_pipe.second
        else:
            temp_pipe = next_pipe.first
        temp_pipe.in_loop = True
        current_pipe, next_pipe = next_pipe, temp_pipe
        path_length += 1

    return path_length


def check_if_enclosed_in_loop(puzzle_map: Map, x: int, y: int) -> bool:
    """
    If there is an even number of vertical lines that are part of the loop to the left of the pipe,
    it is enclosed in the loop."""
    vertical_lines = 0
    last_char = ""

    for x_check in range(x):
        pipe = puzzle_map[x_check][y]
        if pipe.in_loop:
            if pipe.char == "|":
                vertical_lines += 1
            elif pipe.char in "LF":
                last_char = pipe.char
            elif (pipe.char == "7" and last_char == "L") or (pipe.char == "J" and last_char == "F"):
                vertical_lines += 1

    return vertical_lines % 2 == 1


def solve_puzzle_1(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 1.
    """
    puzzle_input = get_input(puzzle_input)
    start_pos, puzzle_map = process_input(puzzle_input)
    return walk_path(puzzle_map, start_pos) // 2


def solve_puzzle_2(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 2.
    """
    puzzle_input = get_input(puzzle_input)
    start_pos, puzzle_map = process_input(puzzle_input)
    walk_path(puzzle_map, start_pos)

    x_map = puzzle_map["x"]
    y_map = puzzle_map["y"]

    score = 0
    for x in range(x_map):
        for y in range(y_map):
            pipe = puzzle_map[x][y]
            if not pipe.in_loop and check_if_enclosed_in_loop(puzzle_map, x, y):
                score += 1

    return score


if __name__ == "__main__":
    solution_1 = solve_puzzle_1()
    print(f"The solution for puzzle 1 is: {solution_1}")

    solution_2 = solve_puzzle_2()
    print(f"The solution for puzzle 2 is: {solution_2}")
