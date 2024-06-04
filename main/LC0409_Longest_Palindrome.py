class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_map = {}

        for c in s:
            if c not in count_map:
                count_map[c] = 0

            count_map[c] += 1

        # print(count_map)

        even_count = 0
        max_odd_value = 0

        for _, value in count_map.items():
            if value % 2 == 0:
                even_count += value
            else:
                max_odd_value = max(max_odd_value, value)

        return even_count + max_odd_value
