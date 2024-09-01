from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        result = []
        row = []
        for i, num in enumerate(original):
            row.append(num)
            if i % n == n - 1:
                result.append(row)
                row = []

        return result

