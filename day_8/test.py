import unittest

from main import solve_puzzle_1, solve_puzzle_2


def get_test_input(test_no: int = 1):
    with open(f"day_8/input/test_{test_no}.txt", "r") as f:
        return f.read().splitlines()


class TestDay0(unittest.TestCase):
    def test_puzzle_1(self):
        test_input = get_test_input(1)
        solution = solve_puzzle_1(test_input)
        self.assertEqual(solution, 6)

    def test_puzzle_2(self):
        test_input = get_test_input(2)
        solution = solve_puzzle_2(test_input)
        self.assertEqual(solution, 6)


if __name__ == "__main__":
    unittest.main()
