import unittest

from main.LC0611_Image_Smoother import LC0611_Image_Smoother

test = LC0611_Image_Smoother()


class LC0242_Valid_Anagram_Test(unittest.TestCase):
    def test_imageSmoother(self):
        self.assertEqual(test.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertEqual(test.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]), [[137, 141, 137], [141, 138, 141], [137, 141, 137]])


