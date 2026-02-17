import unittest

from main.LC0401_Binary_Watch import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findDuplicates(self):
        self.assertEqual(test.readBinaryWatch(1), ["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"])
        self.assertEqual(test.readBinaryWatch(9), [])

