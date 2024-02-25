import collections
from heapq import *
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flightDictionary = collections.defaultdict(dict)
        for start, end, price in flights:
            flightDictionary[start][end] = price

        heap = [(0, src, k + 1)]
        visited = [0] * n
        while heap:
            price, start, remainedCount = heappop(heap)
            if start == dst:
                return price

            if visited[start] >= remainedCount:
                continue

            visited[start] = remainedCount
            for nextStart, nextPrice in flightDictionary[start].items():
                heappush(heap, (price + nextPrice, nextStart, remainedCount - 1))

        return -1