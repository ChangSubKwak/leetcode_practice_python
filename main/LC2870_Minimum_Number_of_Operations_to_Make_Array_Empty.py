from typing import List


class LC2870_Minimum_Number_of_Operations_to_Make_Array_Empty:
    def minOperations(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        maxValue = 0
        for key, value in count.items():
            maxValue = max(maxValue, value)
            if value == 1:
                return -1

        dp = [float('inf')] * (maxValue + 1)

        for i in range(2, maxValue + 1, 2):
            dp[i] = int(i / 2)

        for i in range(3, maxValue + 1, 3):
            dp[i] = int(i / 3)

        for i in range(5, maxValue + 1, 5):
            dp[i] = int(i / 5) * 2

        for i in range(5, maxValue + 1, 1):
            dp[i] = min(dp[i], dp[i - 2] + 1, dp[i - 3] + 1)

        result = 0
        for key, value in count.items():
            result += dp[value]

        return int(result)

