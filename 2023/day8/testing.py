import unittest
from solution import get_step_count, multiple_nodes

class YourTests(unittest.TestCase):

    def test_case_1(self):
        input_data = "RL\n\nAAA = (BBB, CCC)\nBBB = (DDD, EEE)\nCCC = (ZZZ, GGG)\nDDD = (DDD, DDD)\nEEE = (EEE, EEE)\nGGG = (GGG, GGG)\nZZZ = (ZZZ, ZZZ)"
        expected_output = 2
        result = get_step_count(input_data)
        self.assertEqual(result, expected_output)

    def test_case_2(self):
        input_data = "LLR\n\nAAA = (BBB, BBB)\nBBB = (AAA, ZZZ)\nZZZ = (ZZZ, ZZZ)"
        expected_output = 6
        result = get_step_count(input_data)
        self.assertEqual(result, expected_output)

    def test_case3(self):
        input_data = "LR\n\n11A = (11B, XXX)\n11B = (XXX, 11Z)\n11Z = (11B, XXX)\n22A = (22B, XXX)\n22B = (22C, 22C)\n22C = (22Z, 22Z)\n22Z = (22B, 22B)\nXXX = (XXX, XXX)"
        expected_output = 6
        result = multiple_nodes(input_data)
        self.assertEqual(result, expected_output)


# Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
