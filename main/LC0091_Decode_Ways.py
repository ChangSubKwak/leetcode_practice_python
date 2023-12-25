from typing import List


class LC0091_Decode_Ways:
    def doRecursion(self, s: str, dp: List, start: int):
        if start == len(s):
            return 1

        if dp[start] != -1:
            return dp[start]

        if s[start] == "0":
            return 0

        count = self.doRecursion(s, dp, start + 1)
        if start + 1 < len(s) and int(s[start:start + 2]) <= 26:
            count += self.doRecursion(s, dp, start + 2)

        dp[start] = count

        return count

    def numDecodings(self, s: str) -> int:
        dp = [-1 for _ in range(len(s))]
        return self.doRecursion(s, dp, 0)
