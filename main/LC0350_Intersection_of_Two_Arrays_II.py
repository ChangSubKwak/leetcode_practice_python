from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_count1 = {}
        nums_count2 = {}

        for num in nums1:
            nums_count1[num] = nums_count1.get(num, 0) + 1

        for num in nums2:
            nums_count2[num] = nums_count2.get(num, 0) + 1

        if len(nums_count1) < len(nums_count2):
            nums_count1, nums_count2 = nums_count2, nums_count1

        result = []
        for key, value in nums_count1.items():
            if key in nums_count2:
                iteration = min(value, nums_count2[key])

                for i in range(iteration):
                    result.append(key)

        print(result)

        return result
