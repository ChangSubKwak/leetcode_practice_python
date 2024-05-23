from typing import List


class Solution:
    def __init__(self):
        self.result = 0

    def recur(self, nums, k, start, current):
        length = len(nums)

        if start >= length:
            return

        for i in range(start, length):
            current.append(nums[i])

            if len(current) == 1:
                self.result += 1
            else:
                isBeautiful = True
                for j in range(len(current) - 1):
                    if abs(current[-1] - current[j]) == k:
                        isBeautiful = False
                        break

                if not isBeautiful:
                    del current[-1]
                    continue

                self.result += 1

            self.recur(nums, k, i + 1, current)
            del current[-1]

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.result = 0
        self.recur(nums, k, 0, [])

        return self.result