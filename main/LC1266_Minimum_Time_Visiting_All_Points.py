from typing import List


class LC1266_Minimum_Time_Visiting_All_Points:
  def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    length = len(points)
    elapsed_time = 0

    for i in range(length - 1):
      x1 = points[i][0]
      y1 = points[i][1]
      x2 = points[i + 1][0]
      y2 = points[i + 1][1]

      absolute_x = abs(x2 - x1)
      absolute_y = abs(y2 - y1)

      if absolute_x < absolute_y:
        elapsed_time += absolute_x
        elapsed_time += (absolute_y - absolute_x)
      else:
        elapsed_time += absolute_y
        elapsed_time += (absolute_x - absolute_y)

    return elapsed_time
