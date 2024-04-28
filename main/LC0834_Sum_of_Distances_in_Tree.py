import collections
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = collections.defaultdict(set)
        result = [0] * n
        count = [1] * n

        for start, end in edges:
            tree[start].add(end)
            tree[end].add(start)

        def dfs(root, previous):
            for i in tree[root]:
                if i != previous:
                    dfs(i, root)
                    count[root] += count[i]
                    result[root] += result[i] + count[i]

        def dfs_re_root(root, previous):
            for i in tree[root]:
                if i != previous:
                    result[i] = result[root] - count[i] + n - count[i]
                    dfs_re_root(i, root)

        dfs(0, -1)
        dfs_re_root(0, -1)

        return result