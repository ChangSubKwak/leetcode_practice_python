class Solution:
    def isPanlindrome(self, s, left, right) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def countSubstrings(self, s: str) -> int:
        result = 0
        length = len(s)
        for i in range(length):
            for j in range(i, length, 1):
                if self.isPanlindrome(s, i, j):
                    result += 1

        return result
