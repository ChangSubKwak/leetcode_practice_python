import unittest

from main.LC0950_Reveal_Cards_In_Increasing_Order import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_VowelSpellchecker(self):
        self.assertEqual(test.spellchecker(
            ["KiTe", "kite", "hare", "Hare"],
            ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]
        ), ["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"])

        self.assertEqual(test.spellchecker(
            ["yellow"],
            ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]
        ), ["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"])
