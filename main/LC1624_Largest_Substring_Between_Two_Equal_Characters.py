class LC1624_Largest_Substring_Between_Two_Equal_Characters:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        left = [0] * 26
        right = [0] * 26

        for i in range(26):
            target = chr(97 + i)
            for j in range(len(s)):
                if s[j] == target:
                    left[i] = j
                    break

        for i in range(26):
            target = chr(97 + i)
            for j in range(len(s) - 1, -1, -1):
                if s[j] == target:
                    right[i] = j
                    break

        isExist = False
        for i in range(26):
            if left[i] != right[i] and (left[i] != 0 or right[i] != 0):
                isExist = True
                break

        if not isExist:
            return -1

        maxValue = 0
        for i in range(26):
            maxValue = max(maxValue, right[i] - left[i] - 1)

        return maxValue
