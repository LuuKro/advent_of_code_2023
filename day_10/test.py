import unittest

from main import solve_puzzle_1, solve_puzzle_2


def get_test_input():
    with open("day_10/input/test.txt", "r") as f:
        return f.read().splitlines()


def get_test_input_2():
    with open("day_10/input/test2.txt", "r") as f:
        return f.read().splitlines()


class TestDay0(unittest.TestCase):
    def test_puzzle_1(self):
        test_input = get_test_input()
        solution = solve_puzzle_1(test_input)
        self.assertEqual(solution, 8)

    def test_puzzle_2(self):
        test_input = get_test_input_2()
        solution = solve_puzzle_2(test_input)
        self.assertEqual(solution, 10)


if __name__ == "__main__":
    unittest.main()
