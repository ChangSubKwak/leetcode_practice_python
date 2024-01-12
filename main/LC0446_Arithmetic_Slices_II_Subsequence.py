from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        length = len(nums)
        count = 0
        dp = [{} for _ in range(length)]

        for i in range(1, length):
            for j in range(i):
                difference = nums[i] - nums[j]
                if difference not in dp[i]:
                    dp[i][difference] = 0
                dp[i][difference] += 1

                if difference in dp[j]:
                    dp[i][difference] += dp[j][difference]
                    count += dp[j][difference]

        return count