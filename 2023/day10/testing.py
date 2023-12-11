import unittest
from solution import part_one, part_two

class YourTests(unittest.TestCase):

    def test_case_1(self):
        input_data = ".....\n.S-7.\n.|.|.\n.L-J.\n....."
        expected_output = 4
        result = part_one(input_data)
        self.assertEqual(result, expected_output)

    def test_case_2(self):
        input_data = "-L|F7\n7S-7|\nL|7||\n-L-J|\nL|-JF"
        expected_output = 4
        result = part_one(input_data)
        self.assertEqual(result, expected_output)

    def test_case_3(self):
        input_data = "..F7.\n.FJ|.\nSJ.L7\n|F--J\nLJ..."
        expected_output = 8
        result = part_one(input_data)
        self.assertEqual(result, expected_output)

    
    def test_case_3(self):
        input_data = '...........\n.S-------7.\n.|F-----7|.\n.||.....||.\n.||.....||.\n.|L-7.F-J|.\n.|..|.|..|.\n.L--J.L--J.\n...........'
        expected_output = 4
        result = part_two(input_data)

        self.assertEqual(result, expected_output)

    def test_case_4(self):
        input_data = '.F----7F7F7F7F-7....\n.|F--7||||||||FJ....\n.||.FJ||||||||L7....\nFJL7L7LJLJ||LJ.L-7..\nL--J.L7...LJS7F-7L7.\n....F-J..F7FJ|L7L7L7\n....L7.F7||L7|.L7L7|\n.....|FJLJ|FJ|F7|.LJ\n....FJL-7.||.||||...\n....L---J.LJ.LJLJ...'
        expected_output = 8
        result = part_two(input_data)
        self.assertEqual(result, expected_output)
if __name__ == '__main__':
    unittest.main()
