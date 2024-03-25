from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count_dict = {}
        result = []

        for num in nums:
            if num not in count_dict:
                count_dict[num] = 0
            count_dict[num] += 1

            if count_dict[num] == 2:
                result.append(num)

        return result