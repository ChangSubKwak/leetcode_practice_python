from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3:
            return 0

        if len(grid[0]) < 3:
            return 0

        for i in range(3):
            for j in range(3):
                pass

        return 0