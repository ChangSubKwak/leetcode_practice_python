from typing import List


class Solution:
    def firstUniqChar(self, s: str) -> int:
        charIndex = [-1] * 26
        countChar = [0] * 26

        for i, c in enumerate(s):
            index = ord(c) - ord('a')
            charIndex[index] = i
            countChar[index] += 1

        for c in s:
            index = ord(c) - ord('a')
            if countChar[index] == 1:
                return charIndex[index]

        return -1