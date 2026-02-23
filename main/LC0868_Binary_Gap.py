class Solution:
    def binaryGap(self, n: int) -> int:
        if n <= 2:
            return 0

        binary = bin(n)[2:]

        indices = []
        for i, ch in enumerate(binary):
            if ch == '1':
                indices.append(i)

        # print(indices)

        max_value = 0
        for i in range(len(indices) - 1):
            max_value = max(max_value, indices[i + 1] - indices[i])
            # print(max_value, indices[i + 1] - indices[i])

        return max_value