from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        maxFrequency = 0
        for key, value in count.items():
            maxFrequency = max(maxFrequency, value)

        result = 0
        for key, value in count.items():
            if value == maxFrequency:
                result += value

        return result
