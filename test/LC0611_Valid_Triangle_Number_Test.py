import unittest

from main.LC0611_Valid_Triangle_Number import LC0611_Valid_Triangle_Number

test = LC0611_Valid_Triangle_Number()


class LC0611_Valid_Triangle_Number_Test(unittest.TestCase):
    def test_imageSmoother(self):
        self.assertEqual(test.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertEqual(test.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]), [[137, 141, 137], [141, 138, 141], [137, 141, 137]])


