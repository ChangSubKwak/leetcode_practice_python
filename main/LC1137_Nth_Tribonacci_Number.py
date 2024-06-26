class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [-1] * 38
        dp[0] = 0
        dp[1] = dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

        return dp[n]
