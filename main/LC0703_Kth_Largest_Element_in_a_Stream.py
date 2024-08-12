from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.sorted_nums = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        self.sorted_nums.append(val)
        self.sorted_nums.sort(reverse=True)
        return self.sorted_nums[self.k - 1]