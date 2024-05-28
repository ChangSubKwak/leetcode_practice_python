from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        dict_nums = {}

        for num in nums:
            if num not in dict_nums:
                dict_nums[num] = 0

            dict_nums[num] += 1

        sum_nums = 0
        for i in range(1000, -1, -1):
            if i in dict_nums:
                sum_nums += dict_nums[i]

            if i == sum_nums:
                return i

        return -1
