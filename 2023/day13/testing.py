import unittest
from solution import get_summary

class YourTests(unittest.TestCase):

    def test_case_1(self):
        input_data = '##..#.#\n###.#.#\n###.#.#\n##..#.#\n#.##.#.\n.#....#\n..#.###\n..#.#.#\n.##..#.\n....###\n###....\n#..#.##\n######.\n.##..##\n#.###.#'.strip().split('\n\n')
        expected_output = 200
        result = get_summary(input_data)
        self.assertEqual(result, expected_output)

    def test_case_2(self):
        input_data = '#.##..##.\n..#.##.#.\n##......#\n##......#\n..#.##.#.\n..##..##.\n#.#.##.#.\n\n#...##..#\n#....#..#\n..##..###\n#####.##.\n#####.##.\n..##..###\n#....#..#'.strip().split('\n\n')
        expected_output = 405
        result = get_summary(input_data)
        self.assertEqual(result, expected_output)

    def test_case_3(self):
        input_data = '..##..#.#.##.#.\n#..#..##.#..#.#\n######..######.\n..#####........\n######.##.##.##\n######.##.##.##\n..#####........\n######..######.\n#.....##.#..#.#'.strip().split('\n\n')
        expected_output = 11
        result = get_summary(input_data)
        self.assertEqual(result, expected_output)

    
if __name__ == '__main__':
    unittest.main()
