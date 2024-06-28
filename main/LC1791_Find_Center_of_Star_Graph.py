from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count_map = {}

        for [u, v] in edges:
            if u not in count_map:
                count_map[u] = 0

            if v not in count_map:
                count_map[v] = 0

            count_map[u] += 1
            count_map[v] += 1

        count_map = sorted(count_map.items(), key=lambda item: item[1], reverse=True)

        return count_map[0][0]
