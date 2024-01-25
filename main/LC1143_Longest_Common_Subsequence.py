class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = map(len, (text1, text2))

        if m < n:
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)
        for c1 in text1:
            prev = 0
            for i, c2 in enumerate(text2):
                prev, dp[i + 1] = dp[i + 1], prev + 1 if c1 == c2 else max(dp[i], dp[i + 1])

        return dp[-1]