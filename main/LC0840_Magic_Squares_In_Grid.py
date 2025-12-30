from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row = len(grid) - 2
        col = len(grid[0]) - 2

        if row <= 0 or col <= 0:
            return 0

        count = 0
        for y in range(row):
            for x in range(col):
                s = set()

                is_break = False
                for i in range(3):
                    for j in range(3):
                        if grid[y + i][x + j] == 0 or grid[y + i][x + j] >= 10:
                            is_break = True
                            break
                        s.add(grid[y + i][x + j])

                    if is_break:
                        break

                if is_break:
                    continue

                if any(x >= 10 or x == 0 for x in s):
                    continue

                if len(s) != 9:
                    continue

                row_sum = sum(grid[y][x:x + 3])
                if row_sum != sum(grid[y + 1][x:x + 3]):
                    continue

                if row_sum != sum(grid[y + 2][x:x + 3]):
                    continue

                if row_sum != sum([r[0] for r in [r[x:x + 1] for r in grid[y:y + 3]]]):
                    continue

                if row_sum != sum([r[0] for r in [r[x + 1:x + 2] for r in grid[y:y + 3]]]):
                    continue

                if row_sum != sum([r[0] for r in [r[x + 2:x + 3] for r in grid[y:y + 3]]]):
                    continue

                digonal0_sum = 0
                digonal1_sum = 0
                for i in range(3):
                    digonal0_sum += grid[y + i][x + i]
                    digonal1_sum += grid[y + i][x + 2 - i]

                if not (row_sum == digonal0_sum == digonal1_sum):
                    continue

                # print(y, x)
                # print(row0_sum, row1_sum, row2_sum, col0_sum, col1_sum, col2_sum, digonal0_sum, digonal1_sum)

                # if row0_sum == row1_sum == row2_sum == col0_sum == col1_sum == col2_sum == digonal0_sum == digonal1_sum:
                # count += 1
                count += 1

        return count