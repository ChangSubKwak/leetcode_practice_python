from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            if grid[i][0] == 0:
                for j in range(col):
                    grid[i][j] = 1 if grid[i][j] == 0 else 0

        for j in range(1, col):
            zero_of_count = 0
            for i in range(row):
                if grid[i][j] == 0:
                    zero_of_count += 1

            if zero_of_count > row - zero_of_count:
                for i in range(row):
                    grid[i][j] = 1 if grid[i][j] == 0 else 0

        result = 0
        for i in range(row):
            binary_string = "0b" + "".join(map(str, grid[i]))
            integer_value = int(binary_string, 2)
            result += integer_value

        return result