from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums, reverse = True)
        print("sorted_nums", sorted_nums)

        for num in sorted_nums:
            if num < 0:
                break
            # print("-num in nums", (-num in nums))
            if -num in nums:
                return num

        return -1
