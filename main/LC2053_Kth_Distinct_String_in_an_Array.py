from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count_dict = {}
        for c in arr:
            count_dict[c] = count_dict.get(c, 0) + 1

        print(count_dict)

        for i in range(len(arr)):
            if count_dict[arr[i]] == 1:
                k -= 1

            if k == 0:
                return arr[i]

        return ""