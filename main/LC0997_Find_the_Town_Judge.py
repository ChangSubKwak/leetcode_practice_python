from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        count = {}
        dataSet = set()
        for a, b in trust:
            dataSet.add(b)
            if b not in count:
                count[b] = 0
            count[b] += 1

        for a, _ in trust:
            if a in dataSet:
                dataSet.remove(a)

        if len(dataSet) != 1:
            return -1

        key = dataSet.pop()
        if count[key] != n - 1:
            return -1

        return key