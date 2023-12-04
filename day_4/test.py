import unittest

from main import solve_puzzle_1, solve_puzzle_2


def get_test_input() -> list[str]:
    """
    Read the input file and return a list of strings.
    Each string represents a line in the input file.
    """
    with open("day_4/input/test.txt", "r") as f:
        return f.read().splitlines()


class TestDay4(unittest.TestCase):
    def test_solve_puzzle_1(self):
        test_input = get_test_input()
        expected = 13
        self.assertEqual(solve_puzzle_1(test_input), expected)

    def test_solve_puzzle_2(self):
        test_input = get_test_input()
        expected = 30
        self.assertEqual(solve_puzzle_2(test_input), expected)


if __name__ == "__main__":
    unittest.main()
