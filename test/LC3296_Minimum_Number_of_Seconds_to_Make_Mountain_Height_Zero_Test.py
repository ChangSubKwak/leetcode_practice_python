import unittest
from main.LC3296_Minimum_Number_of_Seconds_to_Make_Mountain_Height_Zero import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.minNumberOfSeconds(4, [2, 1, 1]), 3)
        self.assertEqual(test.minNumberOfSeconds(10, [3, 2, 2, 4]), 12)
        self.assertEqual(test.minNumberOfSeconds(5, [1]), 15)
