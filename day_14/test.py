import unittest

from main import process_input, roll_one_cycle, solve_puzzle_1, solve_puzzle_2


def get_test_input():
    with open("day_14/input/test.txt", "r") as f:
        return f.read().splitlines()


class TestDay0(unittest.TestCase):
    def test_roll_one_cycle(self):
        test_input = get_test_input()
        puzzle_map = process_input(test_input)
        roll_one_cycle(puzzle_map)
        puzzle_map_string = "\n".join(["".join(line) for line in puzzle_map])

        expected_puzzle_map_string = """.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#...."""

        self.assertEqual(puzzle_map_string, expected_puzzle_map_string)

    def test_puzzle_1(self):
        test_input = get_test_input()
        solution = solve_puzzle_1(test_input)
        self.assertEqual(solution, 136)

    def test_puzzle_2(self):
        test_input = get_test_input()
        solution = solve_puzzle_2(test_input)
        self.assertEqual(solution, 64)


if __name__ == "__main__":
    unittest.main()
