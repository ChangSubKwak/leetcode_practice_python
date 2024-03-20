from typing import List


class Solution:
    @staticmethod
    def leastInterval(tasks: List[str], n: int) -> int:
        count_dict = {}

        for character in tasks:
            if character not in count_dict:
                count_dict[character] = 0
            count_dict[character] += 1

        sorted_dict_order_by_value_desc = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)
        _, largestValue = sorted_dict_order_by_value_desc[0]

        countLargestValue = 0
        countSum = 0
        for _, value in sorted_dict_order_by_value_desc:
            if value == largestValue:
                countLargestValue += 1
            countSum += value

        return max((largestValue - 1) * (n + 1) + countLargestValue, countSum)
