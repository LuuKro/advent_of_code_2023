from collections import defaultdict, OrderedDict

Box = OrderedDict[str, int]
BoxList = defaultdict[Box]


def get_input(puzzle_input: str = None) -> str:
    """
    Read the input file and return a string.
    """
    if puzzle_input:
        return puzzle_input

    with open("day_15/input/input.txt", "r") as f:
        return f.read()


def process_input(puzzle_input: str) -> list[str]:
    """
    Process the input into a list of strings.
    """
    return puzzle_input.split(",")


def hash_word(word: str) -> int:
    """
    Hashes a word and returns the hash value.
    """
    value = 0
    for letter in word:
        value = ((value + ord(letter)) * 17) % 256
    return value


def add_lens(label: str, value: int, boxes: BoxList) -> None:
    """
    Adds a lens to the boxes dictionary.
    """
    box_no = hash_word(label)
    boxes[box_no][label] = value


def remove_lens(label: str, boxes: BoxList) -> None:
    """
    Removes a lens from the boxes dictionary.
    """
    box_no = hash_word(label)
    boxes[box_no].pop(label, None)


def process_lens(lens: str, boxes=BoxList) -> None:
    """
    Processes a lens and adds or removes it from the boxes dictionary.
    """
    if "-" in lens:
        remove_lens(lens[:-1], boxes)
    else:
        label, value = lens.split("=")
        value = int(value)
        add_lens(label, value, boxes)


def calculate_focussing_power(boxes: BoxList) -> int:
    """
    Calculates the total focusing power of the boxes.
    """
    total_strength = 0
    for box_no, box in boxes.items():
        for i, strength in enumerate(box.values(), start=1):
            total_strength += (box_no + 1) * i * strength

    return total_strength


def solve_puzzle_1(puzzle_input: str = None) -> int:
    """
    Solves puzzle 1.
    """
    puzzle_input = get_input(puzzle_input)
    initialization_sequence = process_input(puzzle_input)

    score = 0
    for step in initialization_sequence:
        score += hash_word(step)

    return score


def solve_puzzle_2(puzzle_input: str = None) -> int:
    """
    Solves puzzle 2.
    """
    puzzle_input = get_input(puzzle_input)
    lenses = process_input(puzzle_input)

    boxes = defaultdict(OrderedDict)
    for lens in lenses:
        process_lens(lens, boxes)

    total_strength = calculate_focussing_power(boxes)
    return total_strength


if __name__ == "__main__":
    solution_1 = solve_puzzle_1()
    print(f"The solution for puzzle 1 is: {solution_1}")

    solution_2 = solve_puzzle_2()
    print(f"The solution for puzzle 2 is: {solution_2}")
