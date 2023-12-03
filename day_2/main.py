import re

GameData = list[dict[str, int]]
Game = dict[int, GameData]


def get_input() -> list[str]:
    """
    Read the input file and return a list of strings.
    Each string represents a line in the input file.
    """
    with open("day_2/input/input.txt", "r") as f:
        return f.read().splitlines()


def parse_game_line(line: str) -> GameData:
    """
    Parse a game line and return a dictionary representing the game data.
    """
    game_list = []
    game_no = int(re.search(r"Game (\d+):", line).group(1))

    line = line.split(": ")[1]
    games = line.split("; ")

    for game in games:
        colors = re.findall(r"(\d+) (\w+)", game)
        game_data = {color[1]: int(color[0]) for color in colors}
        game_list.append(game_data)

    return game_no, game_list


def parse_input(game_input: list[str]) -> Game:
    """
    Parse the input and return a dictionary representing the game data.
    """
    games = {
        game_no: game_data
        for game_no, game_data in (parse_game_line(line) for line in game_input)
    }

    return games


def is_possible(game_data: GameData) -> bool:
    """
    Check if a game is possible.
    """
    availabe_cubes = {"red": 12, "green": 13, "blue": 14}

    for game in game_data:
        for color, count in game.items():
            if count > availabe_cubes[color]:
                return False

    return True


def get_game_power(game_data: GameData) -> int:
    """
    Get the power of a game.
    """
    min_cube_count = {"red": 0, "blue": 0, "green": 0}
    for game in game_data:
        for color in min_cube_count:
            if game.get(color, 0) > min_cube_count[color]:
                min_cube_count[color] = game[color]

    power = min_cube_count["red"] * min_cube_count["blue"] * min_cube_count["green"]
    return power


def solve_puzzle_1(game_input: list[str] = None) -> int:
    """
    Solve puzzle 1.
    """
    if game_input is None:
        game_input = get_input()

    score = 0
    games = parse_input(game_input)

    for game_id, game_data in games.items():
        if is_possible(game_data):
            score += game_id

    return score


def solve_puzzle_2(game_input: list[str] = None) -> int:
    """
    Solve puzzle 2.
    """
    if game_input is None:
        game_input = get_input()

    score = 0
    games = parse_input(game_input)

    for game_data in games.values():
        score += get_game_power(game_data)

    return score


if __name__ == "__main__":
    solution_1 = solve_puzzle_1()
    print(f"The calibration value for puzzle 1 is: {solution_1}")
    solution_2 = solve_puzzle_2()
    print(f"The calibration value for puzzle 2 is: {solution_2}")
