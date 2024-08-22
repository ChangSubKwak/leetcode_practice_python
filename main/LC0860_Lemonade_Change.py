from collections import defaultdict
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bills_count = defaultdict(int)

        for bill in bills:
            if bill == 5:
                bills_count[5] += 1
                continue

            if bill == 10:
                if bills_count[5] == 0:
                    return False

                bills_count[10] += 1
                bills_count[5] -= 1
                continue

            if bill == 20:
                if bills_count[10] >= 1 and bills_count[5] >= 1:
                    bills_count[20] += 1
                    bills_count[10] -= 1
                    bills_count[5] -= 1
                    continue

                if bills_count[5] >= 3:
                    bills_count[20] += 1
                    bills_count[5] -= 3
                    continue

                return False

        return True