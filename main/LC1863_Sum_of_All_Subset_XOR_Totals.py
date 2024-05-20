from typing import List


class Solution:
    def recur(self, nums, current, pos, depth, select_count, xor_value):
        if depth > select_count:
            return

        for i in range(pos, len(nums)):
            current.append(nums[i])
            xor_value ^= nums[i]
            self.sum += xor_value
            self.recur(nums, current, i + 1, depth + 1, select_count, xor_value)
            del current[-1]
            xor_value ^= nums[i]

    def subsetXORSum(self, nums: List[int]) -> int:
        # for i in range(1, len(nums) + 1):
        self.sum = 0
        self.recur(nums, [], 0, 0, len(nums), 0)

        # print("self.sum", self.sum)

        return self.sum
