from collections import defaultdict
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        array_dict = defaultdict(int)

        min_array = []
        max_array = []

        for array in arrays:
            min_max = tuple([min(array), max(array)])
            array_dict[min_max] += 1
            min_array.append(min_max)
            max_array.append(min_max)

        # print(array_dict)

        min_array.sort(key=lambda x: x[0])
        max_array.sort(key=lambda x: x[1])

        left_value = min_array[0][0]
        right_value = max_array[-1][1]

        # print(f"left_value : {left_value}, right_value : {right_value}")

        if array_dict[(left_value, right_value)] == 1:
            next_left_value = min_array[0][0] if len(min_array) <= 1 else min_array[1][0]
            next_right_value = max_array[-1][1] if len(min_array) <= 1 else max_array[-2][1]
            return max(abs(next_left_value - right_value), abs(left_value - next_right_value))

        return abs(left_value - right_value)
