from typing import List


class LC2482_Difference_Between_Ones_and_Zeros_in_Row_and_Column:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rowSize = len(grid)
        colSize = len(grid[0])

        zeroRow = [0 for _ in range(rowSize)]
        zeroCol = [0 for _ in range(colSize)]

        for i in range(rowSize):
            count = 0
            for j in range(colSize):
                if grid[i][j] == 0:
                    count += 1
            zeroRow[i] = count

        for j in range(colSize):
            count = 0
            for i in range(rowSize):
                if grid[i][j] == 0:
                    count += 1
            zeroCol[j] = count

        result = [[0 for _ in range(colSize)] for _ in range(rowSize)]
        for i in range(rowSize):
            for j in range(colSize):
                result[i][j] = rowSize + colSize - 2 * zeroRow[i] - 2 * zeroCol[j]

        return result
