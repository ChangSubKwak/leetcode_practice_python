import numpy as np

class Solution:
    def recursion(self, m, n, maxMove, y, x, moveCount):
        if moveCount > maxMove:
            return

        if y == -1 or x == -1 or y == m or x == n:
            return

        if moveCount > 0:
            self.dp[y][x][moveCount - 1] += 1

        self.recursion(m, n, maxMove, y + 1, x, moveCount + 1)
        self.recursion(m, n, maxMove, y - 1, x, moveCount + 1)
        self.recursion(m, n, maxMove, y, x + 1, moveCount + 1)
        self.recursion(m, n, maxMove, y, x - 1, moveCount + 1)

        return

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # self.dp = np.zeros((m, n, maxMove), dtype=int)
        self.dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)]
        self.recursion(m, n, maxMove, startRow, startColumn, 0)
        print(self.dp)

        return 12