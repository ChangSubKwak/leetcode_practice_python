from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        original_nums = {}
        for i, num in enumerate(nums):
            original_nums[num] = i

        converted_nums = []
        for num in nums:
            str_num = str(num)
            new_num = 0

            length = len(str_num)
            for i, digit in enumerate(list(str_num)):
                # print(i, digit)
                new_num += mapping[int(digit)] * 10 ** (length - i - 1)

            converted_nums.append([new_num, original_nums[num], num])

        sorted_nums = sorted(converted_nums, key=lambda item: (item[0], item[1]))

        return [sub_array[2] for sub_array in sorted_nums]