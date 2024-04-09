from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        length = len(tickets)
        count = 0

        i = 0
        while True:
            if tickets[i] == 0:
                i += 1
                i %= length
                continue

            tickets[i] -= 1
            i += 1
            i %= length
            count += 1

            if tickets[k] == 0:
                break

        return count