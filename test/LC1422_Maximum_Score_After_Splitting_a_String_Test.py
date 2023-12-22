import unittest

from main.LC1422_Maximum_Score_After_Splitting_a_String import LC1422_Maximum_Score_After_Splitting_a_String

test = LC1422_Maximum_Score_After_Splitting_a_String()


class LC1422_Maximum_Score_After_Splitting_a_String_test(unittest.TestCase):
    def test_maxScore(self):
        self.assertEqual(test.maxScore("011101"), 5)
        self.assertEqual(test.maxScore("00111"), 5)
        self.assertEqual(test.maxScore("1111"), 3)



