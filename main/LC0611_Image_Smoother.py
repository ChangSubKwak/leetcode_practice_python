from math import floor
from typing import List


class LC0611_Image_Smoother:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rowSize = len(img)
        colSize = len(img[0])
        smoothedResult = [[0 for _ in range(colSize)] for _ in range(rowSize)]
        direction = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]

        for y in range(rowSize):
            for x in range(colSize):
                count = 0
                sum = 0
                for i, j in direction:
                    if y + i < 0 or y + i >= rowSize or x + j < 0 or x + j >= colSize:
                        continue
                    sum += img[y + i][x + j]
                    count += 1
                smoothedResult[y][x] = floor(sum / count)

        return smoothedResult