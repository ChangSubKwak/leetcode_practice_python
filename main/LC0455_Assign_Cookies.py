from typing import List


class LC0455_Assign_Cookies:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        count = 0
        gIndex = 0
        sIndex = 0

        while gIndex < len(g) and sIndex < len(s):
            if g[gIndex] <= s[sIndex]:
                gIndex += 1
                sIndex += 1
                count += 1
                continue

            sIndex += 1

        return count