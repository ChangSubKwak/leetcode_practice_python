import unittest

from main.LC2169_Count_Operations_to_Obtain_Zero import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_numberOfBeams(self):
        self.assertEqual(test.countOperations(2, 3), 3)
        self.assertEqual(test.countOperations(10, 10), 1)
