import unittest
from main.LC0648_Replace_Words import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_replaceWords(self):
        self.assertEqual(test.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery"), "the cat was rat by the bat")
        self.assertEqual(test.replaceWords(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs"), "aadsfasf absbs bbab cadsfafs")
