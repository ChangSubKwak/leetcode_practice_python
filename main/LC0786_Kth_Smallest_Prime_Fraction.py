from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fractions = []
        length = len(arr)

        for i in range(length):
            for j in range(i + 1, length):
                fractions.append([arr[i], arr[j]])

        fractions = sorted(fractions, key=lambda x: x[0] / x[1])

        return fractions[k - 1]