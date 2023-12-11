def get_input(puzzle_input: list[str] = None) -> list[str]:
    """
    Read the input file and return a list of strings.
    Each string represents a line in the input file.
    """
    if puzzle_input:
        return puzzle_input

    with open("day_9/input/input.txt", "r") as f:
        return f.read().splitlines()


def process_input(puzzle_input: list[str]) -> list[list[int]]:
    """
    Process the input into a list of lists of integers.
    """
    return [[int(num) for num in line.split()] for line in puzzle_input]


def find_differences(numbers: list[int]) -> list[int]:
    """
    Find the differences between each number in the list.
    """
    return [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]


def find_next_number(numbers: list[int]) -> int:
    """
    Find the next number in the sequence.
    """
    differences = find_differences(numbers)
    if all(difference == 0 for difference in differences):
        return numbers[-1]
    else:
        return numbers[-1] + find_next_number(differences)


def find_previous_number(numbers: list[int]) -> int:
    """
    Find the previous number in the sequence.
    """
    differences = find_differences(numbers)
    if all(difference == 0 for difference in differences):
        return numbers[0]
    else:
        return numbers[0] - find_previous_number(differences)


def solve_puzzle_1(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 1.
    """
    puzzle_input = get_input(puzzle_input)
    lines = process_input(puzzle_input)
    return sum(find_next_number(line) for line in lines)


def solve_puzzle_2(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 2.
    """
    puzzle_input = get_input(puzzle_input)
    lines = process_input(puzzle_input)
    return sum(find_previous_number(line) for line in lines)


if __name__ == "__main__":
    solution_1 = solve_puzzle_1()
    print(f"The solution for puzzle 1 is: {solution_1}")

    solution_2 = solve_puzzle_2()
    print(f"The solution for puzzle 2 is: {solution_2}")
