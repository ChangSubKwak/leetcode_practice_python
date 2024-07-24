from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        nums_dict = dict(sorted(nums_dict.items(), key=lambda item: (item[1], -item[0])))

        answer = []
        for key, value in nums_dict.items():
            answer += [key] * value

        return answer
