from typing import List


class LC0455_Assign_Cookies:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        return 1