from typing import List
import copy

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = copy.deepcopy(heights)
        sorted_heights.sort()

        print(heights)
        print(sorted_heights)

        count = 0
        for i, height in enumerate(heights):
            if sorted_heights[i] != height:
                count += 1

        return count
