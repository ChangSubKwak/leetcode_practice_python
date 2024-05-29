class Solution:
    def numSteps(self, s: str) -> int:
        converted_int = int(s, 2)

        count = 0
        while converted_int != 1:
            if converted_int % 2 == 1:
                converted_int += 1
            else:
                converted_int //= 2

            count += 1

        return count
