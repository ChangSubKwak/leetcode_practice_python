from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        length = len(nums)
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        result = nums[0]
        for key, value in count.items():
            if value > (length / 2):
                result = key
                break

        return result