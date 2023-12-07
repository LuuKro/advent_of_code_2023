import math


class Hand:
    """
    Represents a hand of cards.

    Attributes:
        cards (str): The cards in the hand.
        bet (int): The bet placed on the hand.
        strength (int): The strength of the hand.
        type (str): The type of the hand.
    """

    def __init__(self, cards: str, bet: int, with_jokers: bool = False):
        self.cards = cards
        self.bet = bet
        self.strength = convert_cards_to_strength(self.cards, with_jokers)
        self.type = get_hand_type(self.cards, with_jokers)

    def __lt__(self, other):
        return self.strength < other.strength

    def __le__(self, other):
        return self.strength <= other.strength

    def __eq__(self, other):
        return self.strength == other.strength

    def __ge__(self, other):
        return self.strength >= other.strength

    def __gt__(self, other):
        return self.strength > other.strength


def get_input(puzzle_input: list[str] = None) -> list[str]:
    """
    Read the input file and return a list of strings.
    Each string represents a line in the input file.
    """
    if puzzle_input:
        return puzzle_input

    with open("day_7/input/input.txt", "r") as f:
        return f.read().splitlines()


def process_input(puzzle_input: list[str], with_jokers) -> list[Hand]:
    """
    Process the input and return a list of hands.
    """
    hands = []
    for line in puzzle_input:
        cards, bet = line.split(" ")
        hands.append(Hand(cards, int(bet), with_jokers))
    return hands


def convert_jokers(cards: str):
    """
    Convert the jokers to the most prevalent card.
    """
    if cards == "JJJJJ":
        return "AAAAA"
    char_count = {}
    for char in cards:
        if char != "J":
            char_count[char] = char_count.get(char, 0) + 1
    most_prevalent_card = max(char_count, key=char_count.get, default="A")
    return cards.replace("J", most_prevalent_card, -1)


def convert_cards_to_strength(cards: str, with_jokers: bool) -> int:
    """
    Convert a string of cards to a strength.
    """
    if with_jokers:
        card_values = {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 1,
            "T": 10,
        }
    else:
        card_values = {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 11,
            "T": 10,
        }
    strength = 0
    for i, card in enumerate(cards):
        card_value = card_values[card] if card in card_values else int(card)
        strength += card_value * math.pow(10, 9 - i * 2)
    return strength


def get_hand_type(cards: str, with_jokers: bool) -> int:
    """
    Return the type of hand. The higher the number, the better the hand.
    """
    if with_jokers:
        cards = convert_jokers(cards)
    cards = sorted(cards)
    # Five of a kind
    if cards[0] == cards[1] == cards[2] == cards[3] == cards[4]:
        return 6
    # Four of a kind
    elif (cards[0] == cards[1] == cards[2] == cards[3]) or (
        cards[1] == cards[2] == cards[3] == cards[4]
    ):
        return 5
    # Full house
    elif ((cards[0] == cards[1] == cards[2]) and (cards[3] == cards[4])) or (
        (cards[0] == cards[1]) and (cards[2] == cards[3] == cards[4])
    ):
        return 4
    # Three of a kind
    elif (
        (cards[0] == cards[1] == cards[2])
        or (cards[1] == cards[2] == cards[3])
        or (cards[2] == cards[3] == cards[4])
    ):
        return 3
    # Two pairs
    elif ((cards[0] == cards[1]) and ((cards[2] == cards[3]) or (cards[3] == cards[4]))) or (
        (cards[1] == cards[2]) and (cards[3] == cards[4])
    ):
        return 2
    # One pair
    elif (
        (cards[0] == cards[1])
        or (cards[1] == cards[2])
        or (cards[2] == cards[3])
        or (cards[3] == cards[4])
    ):
        return 1
    # High card
    else:
        return 0


def solve_puzzle(puzzle_input: list[str], with_jokers: bool = False):
    """
    Solves the puzzle.
    """
    hands = process_input(puzzle_input, with_jokers)

    hand_types = [[] for _ in range(7)]
    for hand in hands:
        hand_types[hand.type].append(hand)

    sorted_hands = []
    for hand_type in hand_types:
        sorted_hands.extend(sorted(hand_type))

    score = sum([hand.bet * i for i, hand in enumerate(sorted_hands, start=1)])

    return score


def solve_puzzle_1(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 1.
    """
    puzzle_input = get_input(puzzle_input)

    return solve_puzzle(puzzle_input)


def solve_puzzle_2(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 2.
    """
    puzzle_input = get_input(puzzle_input)

    return solve_puzzle(puzzle_input, with_jokers=True)


if __name__ == "__main__":
    solution_1 = solve_puzzle_1()
    print(f"The solution for puzzle 1 is: {solution_1}")

    solution_2 = solve_puzzle_2()
    print(f"The solution for puzzle 2 is: {solution_2}")
