from copy import deepcopy
from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apple.sort(reverse=True)
        capacity.sort(reverse=True)
        capacity_origin = deepcopy(capacity)

        apple_index = 0
        capacity_index = 0
        count = 0

        while apple_index < len(apple):
            if apple[apple_index] - capacity[capacity_index] == 0:
                capacity[capacity_index] = 0
                apple_index += 1
                capacity_index += 1
                continue

            if apple[apple_index] - capacity[capacity_index] > 0:
                apple[apple_index] -= capacity[capacity_index]
                capacity[capacity_index] = 0
                capacity_index += 1
                continue

            if apple[apple_index] - capacity[capacity_index] < 0:
                capacity[capacity_index] -= apple[apple_index]
                apple[apple_index] = 0
                apple_index += 1
                continue

        count = 0
        for i in range(len(capacity)):
            if capacity[i] != capacity_origin[i]:
                count += 1
                continue

            break

        return count