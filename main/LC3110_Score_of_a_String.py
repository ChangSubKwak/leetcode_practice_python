class Solution:
    def scoreOfString(self, s: str) -> int:
        length = len(s)

        result = 0
        for i in range(length - 1):
            result += abs(ord(s[i]) - ord(s[i + 1]))

        return result