from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count_map = {}

        for num in nums:
            if num not in count_map:
                count_map[num] = 0

            count_map[num] += 1

        result = []
        for key, value in count_map.items():
            if value == 2:
                continue

            result.append(key)

        return result
