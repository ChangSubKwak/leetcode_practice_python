class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) == 1:
            return s

        i = 0
        while i < len(s) - 1:
            first = s[i]
            second = s[i + 1]
            caseOne = first == second.lower() and s[i].islower() and s[i + 1].isupper()
            caseTwo = first.lower() == second and s[i].isupper() and s[i + 1].islower()

            if caseOne or caseTwo:
                s = s[:i] + s[i + 2:]
                i = max(i - 1, 0)
                # print(i, s)
                continue

            i += 1

        return s