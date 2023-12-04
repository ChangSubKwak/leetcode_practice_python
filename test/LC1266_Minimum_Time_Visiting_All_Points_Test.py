import unittest

from main.LC1266_Minimum_Time_Visiting_All_Points import LC1266_Minimum_Time_Visiting_All_Points

test = LC1266_Minimum_Time_Visiting_All_Points()


class LC1266_Minimum_Time_Visiting_All_Points_test(unittest.TestCase):
  def test(self):
    self.assertEqual(test.minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]), 7)
    self.assertEqual(test.minTimeToVisitAllPoints([[3, 2], [-2, 2]]), 5)



