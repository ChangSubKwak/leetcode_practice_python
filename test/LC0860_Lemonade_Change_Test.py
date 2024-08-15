import unittest

from main.LC0860_Lemonade_Change import Solution
test = Solution()


class SolutionTest(unittest.TestCase):
    def test_lemonadeChange(self):
        self.assertEqual(test.lemonadeChange([5, 5, 5, 10, 20]), True)
        self.assertEqual(test.lemonadeChange([5, 5, 10, 10, 20]), False)
