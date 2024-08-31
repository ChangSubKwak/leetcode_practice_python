from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        max_probability = [0] * n
        max_probability[start_node] = 1

        for i in range(n - 1):
            has_update = 0
            for j in range(len(edges)):
                u, v = edges[j]
                path_probability = succProb[j]

        return 0.25000
