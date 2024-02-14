import unittest

from main.LC0169_Majority_Element import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_majorityElement(self):
        self.assertEqual(test.majorityElement([3, 2, 3]), 3)
        self.assertEqual(test.majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)


