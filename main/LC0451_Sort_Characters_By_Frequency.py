
class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1

        # print(count)
        sortedCount = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        # print(sortedCount)

        result = ""
        for key, value in sortedCount.items():
            result += key * value

        return result