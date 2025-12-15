from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        contiguous_list = []

        i = 0
        while i < (len(prices) - 1):

            contiguous_count = 0
            while i < (len(prices) - 1) and prices[i] - prices[i + 1] == 1:
                contiguous_count += 1
                i += 1

            if contiguous_count > 0:
                contiguous_list.append(contiguous_count)

            i += 1

        answer = len(prices)
        for num in contiguous_list:
            answer += int(num * (num + 1) / 2)

        return answer