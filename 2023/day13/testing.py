import unittest
from solution import get_summary

class YourTests(unittest.TestCase):

    def test_case_1(self):
        input_data = '##..#.#\n###.#.#\n###.#.#\n##..#.#\n#.##.#.\n.#....#\n..#.###\n..#.#.#\n.##..#.\n....###\n###....\n#..#.\##\n######.\n.##..##\n#.###.#'.strip().split('\n\n')
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

    
    # def test_case_3(self):
    #     input_data = '...........\n.S-------7.\n.|F-----7|.\n.||.....||.\n.||.....||.\n.|L-7.F-J|.\n.|..|.|..|.\n.L--J.L--J.\n...........'
    #     expected_output = 4
    #     result = part_two(input_data)

    #     self.assertEqual(result, expected_output)

    # def test_case_4(self):
    #     input_data = '.F----7F7F7F7F-7....\n.|F--7||||||||FJ....\n.||.FJ||||||||L7....\nFJL7L7LJLJ||LJ.L-7..\nL--J.L7...LJS7F-7L7.\n....F-J..F7FJ|L7L7L7\n....L7.F7||L7|.L7L7|\n.....|FJLJ|FJ|F7|.LJ\n....FJL-7.||.||||...\n....L---J.LJ.LJLJ...'
    #     expected_output = 8
    #     result = part_two(input_data)
    #     self.assertEqual(result, expected_output)
if __name__ == '__main__':
    unittest.main()
