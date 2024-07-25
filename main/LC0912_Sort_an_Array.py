from typing import List


class Solution:
    def quicksort(self, nums, start, end):
        if start >= end:
            return

        pivot = nums[end]
        left = start
        right = end - 1

        while left < right:
            while nums[left] < pivot:
                left += 1

            while nums[right] > pivot:
                right -= 1

            nums[left], nums[right] = nums[right], nums[left]

        nums[left], pivot = pivot, nums[left]

        self.quicksort(nums, start, left - 1)
        self.quicksort(nums, left + 1, end)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)

        return nums
