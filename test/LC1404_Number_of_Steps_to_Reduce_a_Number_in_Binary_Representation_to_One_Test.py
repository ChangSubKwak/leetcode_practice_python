import unittest
from main.LC1404_Number_of_Steps_to_Reduce_a_Number_in_Binary_Representation_to_One import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_maxScore(self):
        self.assertEqual(test.numSteps("1101"), 6)
        self.assertEqual(test.maxScore("10"), 1)
        self.assertEqual(test.maxScore("1"), 0)



