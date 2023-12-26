import unittest

from main.LC1155_Number_of_Dice_Rolls_With_Target_Sum import LC1155_Number_of_Dice_Rolls_With_Target_Sum

test = LC1155_Number_of_Dice_Rolls_With_Target_Sum()


class LC1155_Number_of_Dice_Rolls_With_Target_Sum_Test(unittest.TestCase):

  def test_numRollsToTarget(self):
    self.assertEqual(test.numRollsToTarget(1, 6, 3), 1)
    self.assertEqual(test.numRollsToTarget(2, 6, 7), 6)
    self.assertEqual(test.numRollsToTarget(3, 6, 12), 25)
    self.assertEqual(test.numRollsToTarget(30, 30, 500), 222616187)
