def get_input(puzzle_input: list[str] = None) -> list[str]:
    """
    Read the input file and return a list of strings.
    Each string represents a line in the input file.
    """
    if puzzle_input:
        return puzzle_input

    with open("day_11/input/input.txt", "r") as f:
        return f.read().splitlines()


def get_empty_lines_and_columns(puzzle_input: list[str]) -> tuple[list[int], list[int]]:
    """
    Find the empty lines and columns in the input.
    """
    empty_lines = []
    empty_columns = []
    for y, line in enumerate(puzzle_input):
        if all(char == "." for char in line):
            empty_lines.append(y)

    for column in range(len(puzzle_input[0])):
        if all(line[column] == "." for line in puzzle_input):
            empty_columns.append(column)

    return empty_lines, empty_columns


def get_galaxy_coords(
    x: int, y: int, empty_lines: list[int], empty_columns: list[int], distance: int
) -> tuple[int, int]:
    """
    Calculate the coordinates of a galaxy after considering empty lines and columns.
    """
    coords = (
        x + sum(distance - 1 for num in empty_columns if num < x),
        y + sum(distance - 1 for num in empty_lines if num < y),
    )
    return coords


def process_input(puzzle_input: list[str], distance: int = 2) -> list[tuple[int, int]]:
    """
    Process the input and return the coordinates of the galaxies.
    """
    empty_lines, empty_columns = get_empty_lines_and_columns(puzzle_input)
    galaxies = []

    for y, line in enumerate(puzzle_input):
        for x, char in enumerate(line):
            if char == ".":
                continue

            coords = get_galaxy_coords(x, y, empty_lines, empty_columns, distance)
            galaxies.append(coords)

    return galaxies


def calculate_shortest_distances(galaxies: list[tuple[int, int]]) -> int:
    """
    Calculate the sum of the shortest distances between all pairs of galaxies.
    """
    shortest_distances = 0
    for galaxy in galaxies:
        for other in galaxies:
            if galaxy == other:
                continue

            distance = abs(galaxy[0] - other[0]) + abs(galaxy[1] - other[1])
            shortest_distances += distance

    return shortest_distances // 2


def solve_puzzle_1(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 1.
    """
    puzzle_input = get_input(puzzle_input)
    galaxies = process_input(puzzle_input)
    return calculate_shortest_distances(galaxies)


def solve_puzzle_2(puzzle_input: list[str] = None, distance=1000000) -> int:
    """
    Solve puzzle 2.
    """
    puzzle_input = get_input(puzzle_input)
    galaxies = process_input(puzzle_input, distance)
    return calculate_shortest_distances(galaxies)


if __name__ == "__main__":
    solution_1 = solve_puzzle_1()
    print(f"The solution for puzzle 1 is: {solution_1}")

    solution_2 = solve_puzzle_2()
    print(f"The solution for puzzle 2 is: {solution_2}")
