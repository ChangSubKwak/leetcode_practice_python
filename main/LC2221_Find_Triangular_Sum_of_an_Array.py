from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        length = len(nums)
        list = nums
        for i in range(length - 1, 0, -1):
            result = []
            for j in range(i):
                result.append((list[j] + list[j + 1]) % 10)
            list = result

        return list[0]
