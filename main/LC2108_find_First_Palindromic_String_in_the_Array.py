from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(word):
            length = len(word)

            i = 0
            while i < (length / 2):
                if word[i] != word[length - 1 - i]:
                    return False
                i += 1

            return True

        result = ""
        for word in words:
            if isPalindrome(word):
                result = word
                break

        return result
