from typing import List
import copy

class Solution:
    result = []

    def recur(self, nums, start, depth, select_count, current):
        if depth > select_count:
            return

        for i in range(start, len(nums)):
            current.append(nums[i])
            # print("current", current)
            self.result.append(copy.deepcopy(current))
            self.recur(nums, i + 1, depth + 1, select_count, current)
            del current[-1]

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = [[]]
        self.recur(nums, 0, 0, len(nums) - 1, [])

        return self.result
