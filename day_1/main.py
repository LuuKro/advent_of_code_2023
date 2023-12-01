import re


def get_input() -> list[str]:
    """
    Read the input file and return a list of strings.
    Each string represents a line in the input file.
    """
    with open("day_1/input/input.txt", "r") as f:
        return f.read().splitlines()


def convert_word_to_int(word: str) -> int:
    """
    Replace the given word with its integer representation. If the word already represents an
    integer, return the word as an integer.
    """
    word_to_digit = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    if word in word_to_digit:
        return word_to_digit[word]
    return int(word)


def get_first_and_last_digits(line: str, include_words=False) -> tuple[int, int]:
    """
    Find the first and last digits (or word representations of numbers) in the given line
    and return them as a tuple of integers.
    """
    regex = (
        r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
        if include_words
        else r"(?=(\d))"
    )

    matches = list(re.finditer(regex, line))

    first_digit = convert_word_to_int(matches[0].group(1))
    last_digit = convert_word_to_int(matches[-1].group(1))

    return first_digit, last_digit


def solve_puzzle(puzzle_input: list[str] = None, use_words: bool = False) -> int:
    """
    Solve puzzle by calculating the sum of calibration numbers using the digits in the given
    input data (and/or words, for puzzle 2). If no input data is provided, read the input file.
    Return the solution as an integer.
    """
    if puzzle_input is None:
        puzzle_input = get_input()

    first_and_last_digits = [
        get_first_and_last_digits(line, use_words) for line in puzzle_input
    ]
    solution = sum((first * 10 + last for first, last in first_and_last_digits))

    return solution


if __name__ == "__main__":
    solution_1 = solve_puzzle()
    print(f"The calibration value for puzzle 1 is: {solution_1}")

    solution_2 = solve_puzzle(use_words=True)
    print(f"The calibration value for puzzle 2 is: {solution_2}")
