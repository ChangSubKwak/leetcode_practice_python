class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) != 2:
            first = ""
            for i in range(0, len(s) - 1):
                first += str((int(s[i]) + int(s[i + 1])) % 10)

            s = first

        print(first)

        return s[0] == s[1]