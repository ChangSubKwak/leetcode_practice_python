import unittest
from main.LC3347_Maximum_Frequency_of_an_Element_After_Performing_Operations_II import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.maxFrequency([1, 4, 5], 1, 2), 2)
        self.assertEqual(test.maxFrequency([5, 11, 20, 20], 5, 1), 2)
