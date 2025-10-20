import unittest
from main.LC2011_Final_Value_of_Variable_After_Performing_Operations import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_timeRequiredToBuy(self):
        self.assertEqual(test.finalValueAfterOperations(["--X","X++","X++"]), 1)
        self.assertEqual(test.finalValueAfterOperations(["++X","++X","X++"]), 3)
        self.assertEqual(test.finalValueAfterOperations(["X++","++X","--X","X--"]), 0)
