import math
import re

# Card no, winning numbers, numbers you have
Card = tuple[int, tuple[int], tuple[int]]


def get_input():
    """
    Read the input file and return a list of strings.
    Each string represents a line in the input file.
    """
    with open("day_4/input/input.txt", "r") as f:
        return f.read().splitlines()


def process_line(line: str) -> Card:
    match = re.match(r"Card +(\d+): +(\d+(?:\s*\d+)*) \| +(\d+(?:\s*\d+)*)", line)

    hand_no = int(match.group(1))
    tuple1 = tuple(map(int, match.group(2).split()))
    tuple2 = tuple(map(int, match.group(3).split()))

    return (hand_no, tuple1, tuple2)


def process_input(puzzle_input: list[str]) -> list[Card]:
    """
    Process the puzzle input and return a list of Cards.
    """
    return [process_line(line) for line in puzzle_input]


def calculate_card_score(cards: list) -> int:
    """
    Calculate the score of a list of cards.
    """
    score = int(math.pow(2, len(cards) - 1) if len(cards) > 0 else 0)
    return score


def find_winning_cards(card: Card) -> int:
    """
    Determine the score of a card.
    """
    winning_numbers = card[1]
    numbers_you_have = card[2]
    winning_numbers_you_have = [
        number for number in winning_numbers if number in numbers_you_have
    ]

    return winning_numbers_you_have


def solve_puzzle_1(puzzle_input=None) -> int:
    """
    Solve puzzle 1.
    """
    if puzzle_input is None:
        puzzle_input = get_input()

    cards = process_input(puzzle_input)
    score = 0

    for card in cards:
        winning_cards_you_have = find_winning_cards(card)
        score += calculate_card_score(winning_cards_you_have)

    return score


def solve_puzzle_2(puzzle_input=None) -> int:
    """
    Solve puzzle 2.
    """
    if puzzle_input is None:
        puzzle_input = get_input()

    score = 0
    cards = process_input(puzzle_input)
    card_count = [1 for _ in cards]

    for i, card in enumerate(cards):
        score += card_count[i]
        winning_cards = find_winning_cards(card)
        for j in range(i + 1, i + 1 + len(winning_cards)):
            if j < len(card_count):
                card_count[j] += card_count[i]

    return score


if __name__ == "__main__":
    solution_1 = solve_puzzle_1()
    print(f"The sum of all the card scores for puzzle 1 is: {solution_1}")
    solution_2 = solve_puzzle_2()
    print(f"The amount of scratch cards for puzzle 2 is: {solution_2}")
