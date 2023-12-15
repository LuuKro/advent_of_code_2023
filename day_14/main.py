import copy

Map = list[list[str]]
cache = {}


def get_input(puzzle_input: list[str] = None) -> list[str]:
    """
    Read the input file and return a list of strings.
    Each string represents a line in the input file.
    """
    if puzzle_input:
        return puzzle_input

    with open("day_14/input/input.txt", "r") as f:
        return f.read().splitlines()


def process_input(puzzle_input: list[str]) -> Map:
    """
    Process the input into a usable format.
    """
    puzzle_map = [list(line) for line in puzzle_input]
    return puzzle_map


def roll_rocks_north(puzzle_map: Map, y):
    for i in range(y):
        north_line = puzzle_map[y - i - 1]
        south_line = puzzle_map[y - i]
        for j in range(len(south_line)):
            if south_line[j] == "O" and north_line[j] == ".":
                puzzle_map[y - i - 1][j] = "O"
                puzzle_map[y - i][j] = "."


def roll_all_rocks_north(puzzle_map: Map) -> list[str]:
    for y in range(1, len(puzzle_map)):
        roll_rocks_north(puzzle_map, y)


def roll_rocks_west(puzzle_map: Map, x):
    for i in range(x):
        west_line = [line[x - i - 1] for line in puzzle_map]
        east_line = [line[x - i] for line in puzzle_map]
        for j in range(len(west_line)):
            if west_line[j] == "." and east_line[j] == "O":
                puzzle_map[j][x - i - 1] = "O"
                puzzle_map[j][x - i] = "."


def roll_all_rocks_west(puzzle_map: Map) -> list[str]:
    for x in range(1, len(puzzle_map[0])):
        roll_rocks_west(puzzle_map, x)


def roll_rocks_south(puzzle_map: Map, y):
    for i in range(y):
        north_line = puzzle_map[y - i - 1]
        south_line = puzzle_map[y - i]
        for j in range(len(north_line)):
            if south_line[j] == "." and north_line[j] == "O":
                puzzle_map[y - i][j] = "O"
                puzzle_map[y - i - 1][j] = "."


def roll_all_rocks_south(puzzle_map: Map) -> list[str]:
    for y in range(len(puzzle_map)):
        roll_rocks_south(puzzle_map, y)


def roll_rocks_east(puzzle_map: Map, x):
    for i in range(x):
        west_line = [line[x - i - 1] for line in puzzle_map]
        east_line = [line[x - i] for line in puzzle_map]
        for j in range(len(west_line)):
            if east_line[j] == "." and west_line[j] == "O":
                puzzle_map[j][x - i] = "O"
                puzzle_map[j][x - i - 1] = "."


def roll_all_rocks_east(puzzle_map: Map) -> list[str]:
    for x in range(len(puzzle_map[0])):
        roll_rocks_east(puzzle_map, x)


def roll_one_cycle(puzzle_map: Map):
    roll_all_rocks_north(puzzle_map)
    roll_all_rocks_west(puzzle_map)
    roll_all_rocks_south(puzzle_map)
    roll_all_rocks_east(puzzle_map)


def calculate_load(puzzle_map: Map) -> int:
    load = 0
    max_line_score = len(puzzle_map)
    for i, line in enumerate(puzzle_map):
        for char in line:
            if char == "O":
                load += max_line_score - i

    return load


def solve_puzzle_1(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 1.
    """
    puzzle_input = get_input(puzzle_input)
    puzzle_map = process_input(puzzle_input)
    roll_all_rocks_north(puzzle_map)

    return calculate_load(puzzle_map)


def solve_puzzle_2(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 2.
    """
    puzzle_input = get_input(puzzle_input)
    puzzle_map = process_input(puzzle_input)

    counter = 0
    puzzle_map_string = "".join(["".join(line) for line in puzzle_map])
    while puzzle_map_string not in cache:
        cache[puzzle_map_string] = counter
        roll_one_cycle(puzzle_map)
        counter += 1
        puzzle_map_string = "".join(["".join(line) for line in puzzle_map])

    cycle = counter - cache[puzzle_map_string]
    remaining_cycles = (1000000000 - counter) // cycle
    counter += remaining_cycles * cycle

    while counter < 1000000000:
        roll_one_cycle(puzzle_map)
        counter += 1

    return calculate_load(puzzle_map)


if __name__ == "__main__":
    solution_1 = solve_puzzle_1()
    print(f"The solution for puzzle 1 is: {solution_1}")

    solution_2 = solve_puzzle_2()
    print(f"The solution for puzzle 2 is: {solution_2}")
