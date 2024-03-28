from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        result = 0
        count_num_dict = {}
        left = 0

        for index, num in enumerate(nums):
            count_num_dict[num] = count_num_dict.get(num, 0) + 1

            if count_num_dict[num] > k:
                left_num = nums[left]
                while left_num != num:
                    count_num_dict[left_num] -= 1
                    left += 1
                    left_num = nums[left]

                count_num_dict[left_num] -= 1
                left += 1

            result = max(result, index - left + 1)

        return result