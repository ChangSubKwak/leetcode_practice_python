from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sum_array = []

        for i in range(n):
            partial_sum = 0
            for j in range(i, n):
                partial_sum += nums[j]
                sum_array.append(partial_sum)

        sorted_sum_array = sorted(sum_array)

        result = 0
        for i in range(left - 1, right):
            result += sorted_sum_array[i]
            result %= 1000_000_007

        return result
