from typing import List


class Solution:
    @staticmethod
    def findMaxLength(nums: List[int]) -> int:
        sum_value_index = {}
        sum_value = 0
        max_length = 0
        for index, num in enumerate(nums):
            if num == 1:
                sum_value += 1
            else:
                sum_value -= 1

            if sum_value == 0:
                max_length = index + 1
            elif sum_value in sum_value_index:
                max_length = max(max_length, index - sum_value_index[sum_value])
            else:
                sum_value_index[sum_value] = index

        return max_length