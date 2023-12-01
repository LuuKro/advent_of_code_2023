import unittest

from main import get_first_and_last_digits, solve_puzzle


def get_test_input():
    with open("day_1/input/test.txt", "r") as f:
        return f.read().splitlines()


def get_test_2_input():
    with open("day_1/input/test2.txt", "r") as f:
        return f.read().splitlines()


class FirstAndLastDigitsTestCase(unittest.TestCase):
    def test_repeating_string(self):
        line = "nineight"
        first, last = get_first_and_last_digits(line, True)
        self.assertEqual(first, 9)
        self.assertEqual(last, 8)


class SolvePuzzleTestCase(unittest.TestCase):
    def test_puzzle_1(self):
        test_input = get_test_input()
        solution = solve_puzzle(test_input)
        self.assertEqual(solution, 142)

    def test_puzzle_2(self):
        test_input = get_test_2_input()
        solution = solve_puzzle(test_input, use_words=True)
        self.assertEqual(solution, 281)


if __name__ == "__main__":
    unittest.main()
