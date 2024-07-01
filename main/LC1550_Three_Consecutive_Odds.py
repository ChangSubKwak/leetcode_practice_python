from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 2:
            return False

        for i in range(0, len(arr) - 2, 1):
            one = arr[i] % 2
            two = arr[i + 1] % 2
            three = arr[i + 2] % 2

            if (one + two + three) == 3:
                return True

        return False
