import unittest

from main import (
    get_empty_lines_and_columns,
    process_input,
    solve_puzzle_1,
    solve_puzzle_2,
)

expected_galaxies = [
    (4, 0),
    (9, 1),
    (0, 2),
    (8, 5),
    (1, 6),
    (12, 7),
    (9, 10),
    (0, 11),
    (5, 11),
]


def get_test_input():
    with open("day_11/input/test.txt", "r") as f:
        return f.read().splitlines()


class TestDay0(unittest.TestCase):
    def test_empty_lines_and_columns(self):
        test_input = get_test_input()
        empty_lines, empty_columns = get_empty_lines_and_columns(test_input)
        self.assertEqual(empty_lines, [3, 7])
        self.assertEqual(empty_columns, [2, 5, 8])

    def test_galaxy_processing(self):
        test_input = get_test_input()
        galaxies = process_input(test_input)
        self.assertEqual(galaxies, expected_galaxies)

    def test_puzzle_1(self):
        test_input = get_test_input()
        solution = solve_puzzle_1(test_input)
        self.assertEqual(solution, 374)

    def test_puzzle_2(self):
        test_input = get_test_input()
        solution = solve_puzzle_2(test_input, 10)
        self.assertEqual(solution, 1030)

        solution_2 = solve_puzzle_2(test_input, 100)
        self.assertEqual(solution_2, 8410)


if __name__ == "__main__":
    unittest.main()
