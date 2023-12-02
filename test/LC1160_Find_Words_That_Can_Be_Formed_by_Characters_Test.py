import unittest

from main.LC1160_Find_Words_That_Can_Be_Formed_by_Characters import LC1160_Find_Words_That_Can_Be_Formed_by_Characters

test = LC1160_Find_Words_That_Can_Be_Formed_by_Characters()


class LC1160_Find_Words_That_Can_Be_Formed_by_Characters_Test(unittest.TestCase):

  def test_1(self):
    self.assertEqual(test.countCharacters(["cat", "bt", "hat", "tree"], "atach"), 6)
    self.assertEqual(test.countCharacters(["hello","world","leetcode"], "welldonehoneyr"), 10)
