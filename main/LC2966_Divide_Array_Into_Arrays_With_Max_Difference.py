from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        print(nums)

        result = []

        for i in range(0, len(nums), 3):
            if abs(nums[i] - nums[i + 1]) > k:
                return []

            if abs(nums[i + 1] - nums[i + 2]) > k:
                return []

            if abs(nums[i] - nums[i + 2]) > k:
                return []

            result.append([nums[i], nums[i + 1], nums[i + 2]])

        return result