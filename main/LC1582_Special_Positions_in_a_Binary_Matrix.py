from typing import List


class LC1582_Special_Positions_in_a_Binary_Matrix:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rowSize = len(mat)
        colSize = len(mat[0])

        rowCount = [0] * rowSize
        colCount = [0] * colSize

        for i in range(rowSize):
            for j in range(colSize):
                if mat[i][j] == 1:
                    rowCount[i] += 1
                    colCount[j] += 1

        count = 0
        for i in range(rowSize):
            for j in range(colSize):
                if mat[i][j] == 1 and rowCount[i] == 1 and colCount[j] == 1:
                    count += 1

        return count