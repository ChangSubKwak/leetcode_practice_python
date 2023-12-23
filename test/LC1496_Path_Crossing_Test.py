import unittest

from main.LC1496_Path_Crossing import LC1496_Path_Crossing

test = LC1496_Path_Crossing()


class LC1496_Path_Crossing_Test(unittest.TestCase):
    def test_maxScore(self):
        self.assertEqual(test.isPathCrossing("NES"), False)
        self.assertEqual(test.isPathCrossing("NESWW"), True)




