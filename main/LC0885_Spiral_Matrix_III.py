from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        checkTwoCount = 0
        increase = 2
        rotatePoint = [2, 3]

        while rotatePoint[-1] <= 50000:
            rotatePoint.append(rotatePoint[-1] + increase)
            checkTwoCount += 1

            if checkTwoCount == 2:
                checkTwoCount = 0
                increase += 1

        rotatePoint = set(rotatePoint)

        result = []
        y = rStart
        x = cStart

        count = 1
        total = rows * cols

        direction_array = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction_index = 0

        result.append([y, x])

        while len(result) < total:
            y = y + direction_array[direction_index][0]
            x = x + direction_array[direction_index][1]
            count += 1

            if 0 <= y < rows and 0 <= x < cols:
                result.append([y, x])

            if count in rotatePoint:
                direction_index += 1
                direction_index %= 4

        return result