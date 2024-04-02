from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        result = 0
        start = 0
        count_of_max_element_in_window = 0

        for i, num in enumerate(nums):
            if num == max_element:
                count_of_max_element_in_window += 1

            if count_of_max_element_in_window == k:
                while count_of_max_element_in_window == k:
                    if nums[start] == max_element:
                        count_of_max_element_in_window -= 1
                    start += 1

                result += start

        return result
