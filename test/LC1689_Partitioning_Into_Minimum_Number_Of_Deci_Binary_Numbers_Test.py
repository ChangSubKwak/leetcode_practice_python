import unittest

from main.LC1689_Partitioning_Into_Minimum_Number_Of_Deci_Binary_Numbers import Solution

test = Solution()


class Solution(unittest.TestCase):
    def test(self):
        self.assertEqual(test.minPartitions("32"), 3)
        self.assertEqual(test.minPartitions("82734"), 8)
        self.assertEqual(test.minPartitions("27346209830709182346"), 9)
