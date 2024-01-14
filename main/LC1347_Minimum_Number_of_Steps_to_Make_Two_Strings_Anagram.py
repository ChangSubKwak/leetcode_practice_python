class Solution:
    def minSteps(self, s: str, t: str) -> int:
        length = len(t)
        countSource = [0] * 26
        countTarget = [0] * 26

        for i in range(length):
            countSource[ord(s[i]) - 97] += 1
            countTarget[ord(t[i]) - 97] += 1

        # print(countSource)
        # print(countTarget)

        result = 0
        for i in range(26):
            result += abs(countSource[i] - countTarget[i])

        result /= 2

        return int(result)