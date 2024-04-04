import unittest

from main.LC1614_Maximum_Nesting_Depth_of_the_Parentheses import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.maxDepth("(1+(2*3)+((8)/4))+1"), 3)
        self.assertEqual(test.maxDepth("(1)+((2))+(((3)))"), 3)
