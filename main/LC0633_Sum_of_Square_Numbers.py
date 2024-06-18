from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        final_number = int(sqrt(pow(2, 31) - 1))
        final_number = min(final_number, c)

        square_map = set()

        for i in range(final_number + 1):
            square_map.add(i ** 2)

        for i in range(final_number + 1):
            if (c - i ** 2) in square_map:
                return True

        return False