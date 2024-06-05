class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_map = {}

        for c in s:
            if c not in count_map:
                count_map[c] = 0

            count_map[c] += 1

        print(count_map)

        even_count = 0
        odd_count = 0
        isExistOdd = False

        for value in count_map.values():
            if value % 2 == 0:
                even_count += value
            else:
                odd_count += (value - 1)
                isExistOdd = True

        if isExistOdd:
            return even_count + odd_count + 1

        return even_count + odd_count