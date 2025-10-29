class Solution:
    def smallestNumber(self, n: int) -> int:

        i = 0
        left = right = -1

        while True:
            left = pow(2, i) - 1
            right = pow(2, i + 1) - 1

            if left <= n <= right:
                break

            i += 1

        return right