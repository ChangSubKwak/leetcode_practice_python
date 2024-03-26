from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_value = float('inf')
        max_value = 0

        num_set = set()
        for num in nums:
            num_set.add(num)
            if num <= 0:
                continue
            min_value = min(min_value, num)
            max_value = max(max_value, num)

        if min_value != 1:
            return 1

        for i in range(min_value, max_value + 1):
            if i not in num_set:
                return i

        return max_value + 1

