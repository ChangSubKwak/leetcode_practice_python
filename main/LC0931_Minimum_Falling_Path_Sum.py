import copy
import sys
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])

        dp = []
        dp.append(copy.deepcopy(matrix[0]))

        for y in range(1, row):
            dp.append([])
            dp[y] = [0] * col

            for x in range(0, col):
                if x == 0:
                    dp[y][x] = min(dp[y - 1][x] + matrix[y][x], dp[y - 1][x + 1] + matrix[y][x])
                elif x == col - 1:
                    dp[y][x] = min(dp[y - 1][x] + matrix[y][x], dp[y - 1][x - 1] + matrix[y][x])
                else:
                    dp[y][x] = min(dp[y - 1][x] + matrix[y][x], dp[y - 1][x - 1] + matrix[y][x], dp[y - 1][x + 1] + matrix[y][x])

        minValue = sys.maxsize
        for value in dp[row - 1]:
            minValue = min(minValue, value)

        return minValue