from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringMap = {}

        for string in strs:
            sortedString = "".join(sorted(string))

            if sortedString not in stringMap:
                stringMap[sortedString] = []

            stringMap[sortedString].append(string)

        result = []
        for key, value in stringMap.items():
            result.append(sorted(value))

        return result
