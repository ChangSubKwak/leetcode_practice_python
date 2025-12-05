from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        accumulated_sum = 0

        count = 0
        for i in range(len(nums) - 1):
            accumulated_sum += nums[i]
            if (nums_sum -  2*accumulated_sum) % 2 == 0:
                count += 1

            # print(accumulated_sum, (nums_sum -  accumulated_sum), count)

        return count