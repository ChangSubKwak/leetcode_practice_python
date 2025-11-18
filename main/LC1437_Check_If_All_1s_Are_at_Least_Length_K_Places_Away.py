from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        diff_pos = []
        for i in range(len(nums)):
            if nums[i] == 1:
                diff_pos.append(i)

        for i in range(len(diff_pos) - 1):
            if abs(diff_pos[i + 1] - diff_pos[i] - 1) < k:
                return False

        return True
