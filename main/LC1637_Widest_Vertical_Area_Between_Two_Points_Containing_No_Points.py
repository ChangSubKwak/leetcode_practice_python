from typing import List


class LC1637_Widest_Vertical_Area_Between_Two_Points_Containing_No_Points:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        print(points)

        maxValue = 0

        for i in range(len(points) - 1):
            left = points[i][0]
            right = points[i + 1][0]

            maxValue = max(maxValue, right - left)

        return maxValue
