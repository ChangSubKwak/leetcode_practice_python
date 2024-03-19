import unittest

from main.LC0621_Task_Scheduler import Solution


class SolutionTest(unittest.TestCase):

    def test_leastInterval(self):
        self.assertEqual(Solution.leastInterval(["A", "A", "A", "B", "B", "B"], 2), 8)
        self.assertEqual(Solution.leastInterval(["A", "C", "A", "B", "D", "B"], 1), 6)
        self.assertEqual(Solution.leastInterval(["A", "A", "A", "B", "B", "B"], 3), 10)
