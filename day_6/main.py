import math


def get_input() -> list[str]:
    """
    Read the input file and return a list of strings.
    Each string represents a line in the input file.
    """
    with open("day_6/input/input.txt", "r") as f:
        return f.read().splitlines()


def find_min_max_winning_times(t: int, d: int) -> tuple[int, int]:
    """
    Finds the minimum and maximum winning times.
    """
    discriminant = t**2 - 4 * d

    min_time_f = (-t + math.sqrt(discriminant)) / -2
    min_time = int(min_time_f) + 1 if min_time_f.is_integer() else math.ceil(min_time_f)
    max_time_f = (-t - math.sqrt(discriminant)) / -2
    max_time = int(max_time_f) - 1 if max_time_f.is_integer() else math.floor(max_time_f)

    return min_time, max_time


def solve_puzzle_1(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 1.
    """
    if puzzle_input is None:
        puzzle_input = get_input()

    time_values = [int(time_string) for time_string in puzzle_input[0].split()[1:]]
    distance_values = [int(distance_string) for distance_string in puzzle_input[1].split()[1:]]
    races = zip(time_values, distance_values)

    score = 1
    for race in races:
        min_time, max_time = find_min_max_winning_times(*race)
        score *= max_time - min_time + 1

    return score


def solve_puzzle_2(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 2.
    """
    if puzzle_input is None:
        puzzle_input = get_input()

    time_value = int("".join(puzzle_input[0].split()[1:]))
    distance_value = int("".join(puzzle_input[1].split()[1:]))

    min_time, max_time = find_min_max_winning_times(time_value, distance_value)
    score = max_time - min_time + 1

    return score


if __name__ == "__main__":
    solution_1 = solve_puzzle_1()
    print(f"The solution for puzzle 1 is: {solution_1}")

    solution_2 = solve_puzzle_2()
    print(f"The solution for puzzle 2 is: {solution_2}")
