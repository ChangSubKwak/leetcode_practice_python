import unittest

from main.LC1700_Number_of_Students_Unable_to_Eat_Lunch import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_countStudents(self):
        self.assertEqual(test.countStudents([1, 1, 0, 0], [0, 1, 0, 1]), 0)
        self.assertEqual(test.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]), 3)
