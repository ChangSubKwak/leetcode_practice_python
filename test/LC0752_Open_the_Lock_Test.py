import unittest

from main.LC0752_Open_the_Lock import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findErrorNums(self):
        self.assertEqual(test.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"), 6)
        self.assertEqual(test.openLock(["8888"], "0009"), 1)
        self.assertEqual(test.openLock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"), -1)
