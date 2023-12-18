from typing import List


class LC1913_Maximum_Product_Difference_Between_Two_Pairs:
    def maxProductDifference(self, nums: List[int]) -> int:
        length = len(nums)
        nums.sort()

        w = nums[0]
        x = nums[1]
        y = nums[length - 2]
        z = nums[length - 1]

        return y * z - w * x