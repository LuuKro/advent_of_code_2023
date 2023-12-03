# number, (x, y)
Number = tuple[int, tuple[int, int]]
# (x, y)
Symbol = tuple[str, tuple[int, int]]


def get_input() -> list[str]:
    """
    Read the input file and return a list of strings.
    Each string represents a line in the input file.
    """
    with open("day_3/input/input.txt", "r") as f:
        return f.read().splitlines()


def add_number(current_number: str, x: int, y: int, numbers: list[Number]) -> None:
    """
    Add a number to the list of numbers.
    """
    if current_number != "":
        number = (int(current_number), (x, y))
        numbers.append(number)


def process_line(
    y: int, line: str, numbers: list[Number], symbols: list[Symbol]
) -> None:
    """
    Process a line of the input and update the list of numbers and symbols.
    """
    current_number = ""
    for x, char in enumerate(line):
        if char.isnumeric():
            current_number += char
        else:
            if char != ".":
                symbols.append((char, (x, y)))
            add_number(current_number, x - len(current_number), y, numbers)
            current_number = ""
    add_number(current_number, x - len(current_number) + 1, y, numbers)


def process_input(map_input: list[str]) -> (list[Number], list[Symbol]):
    """
    Process the input and return a list of numbers and symbols.
    """
    numbers = []
    symbols = []

    for y, line in enumerate(map_input):
        process_line(y, line, numbers, symbols)

    return numbers, symbols


def is_adjacent_to_symbol(number: Number, symbols: list[Symbol]) -> Symbol | bool:
    """
    Check if a number is adjacent to a symbol.
    """
    value = number[0]
    length = len(str(value))
    x, y = number[1]

    for symbol in symbols:
        x_symbol, y_symbol = symbol[1]

        # More than 1 y-coordinate away
        if abs(y - y_symbol) > 1:
            continue

        # More than 1 x-coordinate away
        if (x_symbol < x - 1) or (x_symbol > (x + length)):
            continue

        return symbol
    return False


def get_all_gears(numbers: list[Number], symbols: list[Symbol]) -> int:
    """
    Extermely inefficient way to get all the gears. I am not proud of this.
    """

    gears = []
    for symbol in symbols:
        if symbol[0] != "*":
            continue

        adjacent_number = []
        x, y = symbol[1]

        for number in numbers:
            adjacent_symbol = is_adjacent_to_symbol(number, symbols)
            if not adjacent_symbol or adjacent_symbol[0] != "*":
                continue
            adjacent_x, adjacent_y = adjacent_symbol[1]
            if x == adjacent_x and y == adjacent_y:
                adjacent_number.append(number[0])

        if len(adjacent_number) == 2:
            gears.append(adjacent_number[0] * adjacent_number[1])

    return sum(gears)


def solve_puzzle_1(map_input: list[str] = None) -> int:
    """
    Solve puzzle 1.
    """
    if map_input is None:
        map_input = get_input()

    numbers, symbols = process_input(map_input)
    numbers_adjacent_to_symbols = [
        number for number in numbers if is_adjacent_to_symbol(number, symbols)
    ]

    return sum([number[0] for number in numbers_adjacent_to_symbols])


def solve_puzzle_2(map_input: list[str] = None) -> int:
    """
    Solve puzzle 2.
    """
    if map_input is None:
        map_input = get_input()

    numbers, symbols = process_input(map_input)
    gears = get_all_gears(numbers, symbols)
    return gears


if __name__ == "__main__":
    solution_1 = solve_puzzle_1()
    print(f"The sum of all the part numbers for puzzle 1 is: {solution_1}")
    solution_2 = solve_puzzle_2()
    print(f"The sum of all gear ratios for puzzle 2 is: {solution_2}")
