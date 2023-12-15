# Springs, groups
Row = tuple[str, tuple[int, ...]]


def get_input(puzzle_input: list[str] = None) -> list[str]:
    """
    Read the input file and return a list of strings.
    Each string represents a line in the input file.
    """
    if puzzle_input:
        return puzzle_input

    with open("day_12/input/input.txt", "r") as f:
        return f.read().splitlines()


def process_input(puzzle_input: list[str], folded=False) -> list[Row]:
    rows = []
    for line in puzzle_input:
        springs, group_str = line.split(" ")
        group = tuple(int(cond) for cond in group_str.split(","))

        if folded:
            springs = ((springs + "?") * 5)[:-1]
            group = group * 5

        rows.append((springs, group))
    return rows


def find_number_of_arrangements(row: Row, cache: dict) -> int:
    springs, groups = row
    if not groups:  # No more groups to find
        return 1 if "#" not in springs else 0

    max_group_start = (
        len(springs) - sum(groups) - len(groups) + 1
    )  # Last possible option for first group to start
    if "#" in springs:
        max_group_start = min(
            springs.index("#"), max_group_start
        )  # If there's an earlier broken spring, that's the last possible option

    arrangements = 0
    for group_start in range(max_group_start + 1):
        group_end = group_start + groups[0]
        potential_group = springs[group_start:group_end]

        if not all(char != "." for char in potential_group):
            continue  # Not a potential valid group

        if group_end > len(springs) or (group_end != len(springs) and springs[group_end] == "#"):
            continue  # Group is not separated from next

        remaining_springs = springs[group_end + 1 :]
        partial_row = (remaining_springs, groups[1:])
        if partial_row not in cache:
            cache[partial_row] = find_number_of_arrangements(partial_row, cache)
        arrangements += cache[partial_row]

    return arrangements


def find_total_arrangements(rows: list[Row]) -> int:
    """
    Find the total number of arrangements.
    """
    arrangements = 0
    cache = {}
    for row in rows:
        arrangements += find_number_of_arrangements(row, cache)

    return arrangements


def solve_puzzle_1(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 1.
    """
    puzzle_input = get_input(puzzle_input)
    rows = process_input(puzzle_input)
    score = find_total_arrangements(rows)

    return score


def solve_puzzle_2(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 2.
    """
    puzzle_input = get_input(puzzle_input)
    rows = process_input(puzzle_input, folded=True)
    score = find_total_arrangements(rows)

    return score


if __name__ == "__main__":
    solution_1 = solve_puzzle_1()
    print(f"The solution for puzzle 1 is: {solution_1}")

    solution_2 = solve_puzzle_2()
    print(f"The solution for puzzle 2 is: {solution_2}")
