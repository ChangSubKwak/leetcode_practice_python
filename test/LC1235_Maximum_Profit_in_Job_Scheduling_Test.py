import unittest

from main.LC1235_Maximum_Profit_in_Job_Scheduling import LC1235_Maximum_Profit_in_Job_Scheduling

test = LC1235_Maximum_Profit_in_Job_Scheduling()


class LC1235_Maximum_Profit_in_Job_Scheduling_Test(unittest.TestCase):
  def test(self):
    self.assertEqual(test.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]), 120)



