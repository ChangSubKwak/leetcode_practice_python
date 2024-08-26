import unittest
from main.LC0590_N_ary_Tree_Postorder_Traversal import Solution

from main.Node import Node

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_postorder1(self):
        root = Node(1)
        root.children = [Node(3), Node(2), Node(4)]
        root.children[0].children = [Node(5), Node(6)]

        self.assertEqual(test.postorder(root), [5, 6, 3, 2, 4, 1])

    def test_postorder2(self):
        root = Node(1)
        root.children = [Node(2), Node(3), Node(4), Node(5)]
        root.children[1].children = [Node(6), Node(7)]
        root.children[1].children[1].children = [Node(11)]
        root.children[1].children[1].children[0].children = [Node(14)]

        root.children[2].children = [Node(8)]
        root.children[2].children[0].children = [Node(12)]

        root.children[3].children = [Node(9), Node(10)]
        root.children[3].children[0].children = [Node(13)]

        self.assertEqual(test.postorder(root), [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1])
