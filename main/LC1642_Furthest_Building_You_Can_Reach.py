from typing import List
from heapq import *


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        length = len(heights)

        for i in range(length - 1):
            difference = heights[i + 1] - heights[i]
            if difference > 0:
                heappush(heap, difference)

            if len(heap) > ladders:
                bricks -= heappop(heap)

            if bricks < 0:
                return i

        return length - 1