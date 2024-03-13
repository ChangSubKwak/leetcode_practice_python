class Solution:
    def customSortString(self, order: str, s: str) -> str:
        countDictionary = [0] * 26
        length = len(order)
        for c in order:
            countDictionary[ord(c) - ord('a')] = length
            length -= 1

        length = len(s)
        slist = list(s)
        for i in range(length - 1):
            for j in range(i, length):
                leftOrder = countDictionary[ord(slist[i]) - ord('a')]
                rightOrder = countDictionary[ord(slist[j]) - ord('a')]

                if leftOrder < rightOrder:
                    slist[i], slist[j] = slist[j], slist[i]

        return "".join(slist)
