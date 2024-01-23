from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        uniqueList = []

        for s in arr:
            setData = set(s)
            if len(set(setData)) == len(s):
                uniqueList.append(set(setData))

        newData = [set()]
        for uniqueData in uniqueList:
            for data in newData:
                if len(uniqueData & data) > 0:
                    continue
                newData.append(uniqueData | data)

        maxLength = 0
        for data in newData:
            maxLength = max(maxLength, len(data))

        return maxLength
