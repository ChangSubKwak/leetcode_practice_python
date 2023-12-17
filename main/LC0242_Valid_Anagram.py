class LC0242_Valid_Anagram:
    def isAnagram(self, s: str, t: str) -> bool:
        sourceCount = [0 for _ in range(26)]
        targetCount = [0 for _ in range(26)]

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sourceIndex = ord(s[i]) - ord('a')
            sourceCount[sourceIndex] += 1

            targetIndex = ord(t[i]) - ord('a')
            targetCount[targetIndex] += 1

        for i in range(26):
            if sourceCount[i] != targetCount[i]:
                return False

        return True