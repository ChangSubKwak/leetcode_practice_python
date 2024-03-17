from typing import List


class Solution:
    @staticmethod
    def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        length = len(intervals)
        result = []
        i = 0

        while i < length and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < length and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1

        result.append(newInterval)

        while i < length:
            result.append(intervals[i])
            i += 1

        return result