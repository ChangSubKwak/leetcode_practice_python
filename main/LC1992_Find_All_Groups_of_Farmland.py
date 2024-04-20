from typing import List


class Solution:
    def recur(self, land, y, x, visited, result):
        if y < 0 or y >= self.row or x < 0 or x >= self.col:
            return

        if visited[y][x]:
            return

        if land[y][x] == 0:
            return

        group_col = 0
        while x + group_col < self.col and land[y][x + group_col] == 1:
            group_col += 1

        group_row = 0
        while y + group_row < self.row and land[y + group_row][x] == 1:
            group_row += 1

        for i in range(group_row):
            for j in range(group_col):
                visited[y + i][x + j] = True

        result.append([y, x, y + group_row - 1, x + group_col - 1])

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        self.row = len(land)
        self.col = len(land[0])

        visited = []
        for i in range(self.row):
            visited.append([])
            for j in range(self.col):
                visited[i].append(False)

        result = []
        for i in range(self.row):
            for j in range(self.col):
                self.recur(land, i, j, visited, result)

        return result