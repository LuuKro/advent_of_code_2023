from functools import cache


def get_input(puzzle_input: list[str] = None) -> str:
    """
    Read the input file and return a list of strings.
    Each string represents a line in the input file.
    """
    if puzzle_input:
        return puzzle_input

    with open("day_13/input/input.txt", "r") as f:
        return f.read()


def process_input(puzzle_input: str) -> list[list[str]]:
    """
    Process the input into a usable format.
    """
    areas = [area.splitlines() for area in puzzle_input.split("\n\n")]
    return areas


def find_differences(first_line: str, second_line: str, with_fudge: bool) -> bool:
    """
    Find the number of differences between two lines.
    """
    if not with_fudge:
        return first_line != second_line

    differences = 0
    for i in range(len(first_line)):
        if first_line[i] != second_line[i]:
            differences += 1
            if differences > 1:
                return differences
    return differences


def check_mirror_line(area: list[str], mirror: int, with_fudge: bool) -> bool:
    """
    Check if a line is a mirror line.
    """
    mirrored, mirror_counter = mirror, mirror - 1
    differences = 0
    while mirror_counter > -1 and mirrored < len(area):
        differences += find_differences(area[mirror_counter], area[mirrored], with_fudge)
        if (differences > 0 and not with_fudge) or differences > 1:
            return False
        mirror_counter -= 1
        mirrored += 1
    return differences == 1 if with_fudge else differences == 0


def find_mirror_line(area: list[str], with_fudge: bool) -> int:
    """
    Find the mirror line in an area.
    """
    for mirror in range(1, len(area)):
        if check_mirror_line(area, mirror, with_fudge):
            return mirror

    return -1


def find_mirror(area: list[str], with_fudge: bool = False) -> tuple[int, bool]:
    """
    Find the mirror in an area. Returns the column/line number and a boolean that's True if it's a
    column.
    """
    if (mirror_line := find_mirror_line(area, with_fudge)) != -1:
        return mirror_line, False
    mirrored_area = ["".join([area[j][i] for j in range(len(area))]) for i in range(len(area[0]))]
    return find_mirror_line(mirrored_area, with_fudge), True


def solve_puzzle_1(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 1.
    """
    puzzle_input = get_input(puzzle_input)
    areas = process_input(puzzle_input)

    score = 0
    for area in areas:
        mirror, is_column = find_mirror(area)
        score += mirror if is_column else mirror * 100

    return score


def solve_puzzle_2(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 2.
    """
    puzzle_input = get_input(puzzle_input)
    areas = process_input(puzzle_input)

    score = 0
    for area in areas:
        mirror, is_column = find_mirror(area, with_fudge=True)
        score += mirror if is_column else mirror * 100

    return score


if __name__ == "__main__":
    solution_1 = solve_puzzle_1()
    print(f"The solution for puzzle 1 is: {solution_1}")

    solution_2 = solve_puzzle_2()
    print(f"The solution for puzzle 2 is: {solution_2}")
