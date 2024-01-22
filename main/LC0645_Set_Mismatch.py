from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        duplicatedKey = 0
        for key, val in count.items():
            if val == 2:
                duplicatedKey = key
                break

        length = len(nums)
        missingKey = 0
        for i in range(1, length + 1):
            if i not in count:
                missingKey = i
                break

        return [duplicatedKey, missingKey]
