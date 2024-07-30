class Solution:
    def minimumDeletions(self, s: str) -> int:
        length = len(s)
        count_of_b_from_left = [0 for _ in range(length)]
        count_of_a_from_right = [0 for _ in range(length)]

        count_of_b = 0
        for i in range(length):
            count_of_b_from_left[i] = count_of_b
            if s[i] == "b":
                count_of_b += 1

        count_of_a = 0
        for i in range(length - 1, -1, -1):
            count_of_a_from_right[i] = count_of_a
            if s[i] == "a":
                count_of_a += 1

        minimum_deletion = length
        for i in range(length):
            minimum_deletion = min(minimum_deletion, count_of_b_from_left[i] + count_of_a_from_right[i])

        print(count_of_b_from_left)
        print(count_of_a_from_right)

        return minimum_deletion