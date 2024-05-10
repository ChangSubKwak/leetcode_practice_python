from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        tuple_list = []
        for index, num in enumerate(score):
            tuple_list.append((num, index))

        tuple_list = sorted(tuple_list, key=lambda x: -x[0])

        grade_map = {}
        for index, element in enumerate(tuple_list):
            grade_map[element[0]] = index

        # print("tuple_list", tuple_list)
        # print("grade_map", grade_map)

        result = []
        for index, num in enumerate(score):
            if grade_map[num] == 0:
                result.append("Gold Medal")
                continue

            if grade_map[num] == 1:
                result.append("Silver Medal")
                continue

            if grade_map[num] == 2:
                result.append("Bronze Medal")
                continue

            result.append(str(grade_map[num] + 1))

        return result