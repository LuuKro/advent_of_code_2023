Mirrors = dict[tuple[int, int], str]  # loc(x, y): type
Beam = tuple[tuple[int, int], tuple[int, int]]  # loc(x, y), dir(x, y)


def get_input(puzzle_input: list[str] = None) -> list[str]:
    """
    Read the input file and return a list of strings.
    Each string represents a line in the input file.
    """
    if puzzle_input:
        return puzzle_input

    with open("day_16/input/input.txt", "r") as f:
        return f.read().splitlines()


def process_input(puzzle_input: list[str]) -> Mirrors:
    """
    Process the input and return a dictionary with the following structure:
    {(x, y): "type"}
    """
    mirrors = {}
    x_max, y_max = len(puzzle_input[0]), len(puzzle_input)
    for y, line in enumerate(puzzle_input):
        for x, char in enumerate(line):
            if char != ".":
                mirrors[(x, y)] = char
    return mirrors, x_max, y_max


def find_new_directions(found_mirror: str, direction: tuple[int, int]) -> tuple[tuple[int, int]]:
    """
    Find the new direction of the beam.
    """
    dx, dy = direction
    if found_mirror in "/\\":
        if found_mirror == "/":
            if dx:
                return ((0, -dx),)
            return ((-dy, 0),)
        if dx:
            return ((0, dx),)
        return ((dy, 0),)

    elif found_mirror in "|-":
        if found_mirror == "|":
            return ((0, -1), (0, 1))
        return ((1, 0), (-1, 0))
    else:
        raise ValueError(f"Unknown mirror type: {found_mirror}")


def process_beam(
    beam: Beam,
    mirrors: Mirrors,
    x_max: int,
    y_max: int,
    calculating: dict,
    cache: dict,
) -> set[tuple[int, int]]:
    """
    Process the beam and return the new beam.
    """

    if beam in cache:
        return cache[beam]
    elif beam in calculating:
        return set()
    calculating[beam] = True

    loc, direction = beam
    x, y = loc
    dx, dy = direction

    found_mirror = None
    visited_locations = set()
    while (-1 < x < x_max) and (-1 < y < y_max) and found_mirror is None:
        visited_locations.add((x, y))
        if (x, y) in mirrors:
            next_mirror = mirrors[(x, y)]
            if not ((dx and next_mirror == "-") or (dy and next_mirror == "|")):
                found_mirror = (x, y)
                break
        x += dx
        y += dy

    if found_mirror is not None:
        new_directions = find_new_directions(next_mirror, direction)
        beams = (
            (
                (found_mirror[0] + new_direction[0], found_mirror[1] + new_direction[1]),
                new_direction,
            )
            for new_direction in new_directions
        )
        for beam in beams:
            new_locations = process_beam(beam, mirrors, x_max, y_max, calculating, cache)
            for location in new_locations:
                if location not in visited_locations:
                    visited_locations.add(location)

    cache[beam] = visited_locations

    return visited_locations


def trace_lightbeam(
    beam: Beam, mirrors: Mirrors, x_max: int, y_max: int, cache: dict
) -> set[tuple[int, int]]:
    cache_calculating = {}  # Beams can loop, so we need to cache the beams we are calculating
    visited_squares = set()

    visited_squares.update(process_beam(beam, mirrors, x_max, y_max, cache_calculating, cache))

    return visited_squares


def count_energized_squares(
    start_beam: Beam, mirrors: Mirrors, x_max: int, y_max: int
) -> set[tuple[int, int]]:
    cache = {}
    visited_squares = trace_lightbeam(start_beam, mirrors, x_max, y_max, cache)
    return len(visited_squares)


def solve_puzzle_1(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 1.
    """
    puzzle_input = get_input(puzzle_input)
    mirrors, x_max, y_max = process_input(puzzle_input)

    start_beam = ((0, 0), (1, 0))
    energized_squares = count_energized_squares(start_beam, mirrors, x_max, y_max)

    return energized_squares


def solve_puzzle_2(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 2.
    """
    puzzle_input = get_input(puzzle_input)
    mirrors, x_max, y_max = process_input(puzzle_input)

    max_energized_squares = 0
    for x in range(x_max):
        for y in (0, y_max - 1):
            yd = -1 if y else 1
            start_beam = ((x, y), (0, yd))
            energized_squares = count_energized_squares(start_beam, mirrors, x_max, y_max)
            if energized_squares > max_energized_squares:
                max_energized_squares = energized_squares

    for y in range(y_max):
        for x in (0, x_max - 1):
            xd = -1 if x else 1
            start_beam = ((x, y), (xd, 0))
            energized_squares = count_energized_squares(start_beam, mirrors, x_max, y_max)
            if energized_squares > max_energized_squares:
                max_energized_squares = energized_squares

    return max_energized_squares


if __name__ == "__main__":
    solution_1 = solve_puzzle_1()
    print(f"The solution for puzzle 1 is: {solution_1}")

    solution_2 = solve_puzzle_2()
    print(f"The solution for puzzle 2 is: {solution_2}")
