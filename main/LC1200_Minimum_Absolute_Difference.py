from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        length = len(arr)
        min_value = 2 * (10 ** 6)
        for i in range(1, length):
            min_value = min(min_value, abs(arr[i - 1] - arr[i]))

        result = []
        for i in range(1, length):
            if min_value == abs(arr[i - 1] - arr[i]):
                first = min(arr[i - 1], arr[i])
                second = max(arr[i - 1], arr[i])
                result.append([first, second])

        return result