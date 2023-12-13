import unittest

from main import find_number_of_arrangements, solve_puzzle_1, solve_puzzle_2


def get_test_input():
    with open("day_12/input/test.txt", "r") as f:
        return f.read().splitlines()


class TestDay0(unittest.TestCase):
    def test_find_arrangements(self):
        cache = {}
        self.assertEqual(find_number_of_arrangements(("???.###", (1, 1, 3)), cache), 1)
        self.assertEqual(find_number_of_arrangements((".??..??...?##.", (1, 1, 3)), cache), 4)
        self.assertEqual(find_number_of_arrangements(("?#?#?#?#?#?#?#?", (1, 3, 1, 6)), cache), 1)
        self.assertEqual(find_number_of_arrangements(("????.#...#...", (4, 1, 1)), cache), 1)
        self.assertEqual(find_number_of_arrangements(("????.######..#####.", (1, 6, 5)), cache), 4)
        self.assertEqual(find_number_of_arrangements(("?###????????", (3, 2, 1)), cache), 10)

    def test_puzzle_1(self):
        test_input = get_test_input()
        solution = solve_puzzle_1(test_input)
        self.assertEqual(solution, 21)

    def test_puzzle_2(self):
        test_input = get_test_input()
        solution = solve_puzzle_2(test_input)
        self.assertEqual(solution, 525152)


if __name__ == "__main__":
    unittest.main()
