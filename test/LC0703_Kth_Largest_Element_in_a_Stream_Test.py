import unittest

from main.LC0703_Kth_Largest_Element_in_a_Stream import KthLargest


class SolutionTest(unittest.TestCase):
    def test_KthLargest(self):
        test = KthLargest(3, [4, 5, 8, 2])
        
        self.assertEqual(test.add(3), 4)
        self.assertEqual(test.add(5), 5)
        self.assertEqual(test.add(10), 5)
        self.assertEqual(test.add(9), 8)
        self.assertEqual(test.add(4), 8)
