import heapq
from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        pq = []

        for happiness_value in happiness:
            heapq.heappush(pq, -happiness_value)

        total = 0
        count = 0
        while pq and k > 0:
            happiness_value = - heapq.heappop(pq)
            total += max(happiness_value - count, 0)
            count += 1
            k -= 1

        return total
