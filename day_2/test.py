import unittest

from main import parse_game_line, solve_puzzle_1, solve_puzzle_2


def get_test_input() -> list[str]:
    """
    Read the input file and return a list of strings.
    Each string represents a line in the input file.
    """
    with open("day_2/input/test.txt", "r") as f:
        return f.read().splitlines()


class TestDay2(unittest.TestCase):
    def test_parse_game_line(self):
        line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        game_data = parse_game_line(line)
        expected = (
            1,
            [{"blue": 3, "red": 4}, {"blue": 6, "red": 1, "green": 2}, {"green": 2}],
        )
        self.assertEqual(game_data, expected)

    def test_solve_puzzle_1(self):
        game_data = get_test_input()
        expected = 8
        self.assertEqual(solve_puzzle_1(game_data), expected)

    def test_solve_puzzle_2(self):
        game_data = get_test_input()
        expected = 2286
        self.assertEqual(solve_puzzle_2(game_data), expected)


if __name__ == "__main__":
    unittest.main()
