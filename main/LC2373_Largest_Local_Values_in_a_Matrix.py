from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])

        result = [[0 for _ in range(col - 2)] for _ in range(row - 2)]

        for i in range(1, row - 1):
            for j in range(1, col - 1):
                result[i - 1][j - 1] = max(
                    grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1],
                    grid[i][j - 1], grid[i][j], grid[i][j + 1],
                    grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1]
                )

        return result
