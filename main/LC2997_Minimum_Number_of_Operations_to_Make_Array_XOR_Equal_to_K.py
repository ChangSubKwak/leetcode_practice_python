from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        final_value = nums[0]
        for i in range(1, len(nums)):
            final_value ^= nums[i]
        final_binary_value = bin(final_value)[2:]

        binary_k = bin(k)[2:]
        width = max(len(final_binary_value), len(binary_k))

        final_binary_value = f'{final_value:0{width}b}'
        binary_k = f'{k:0{width}b}'

        # print("final_binary_value", final_binary_value)
        # print("binary_k", binary_k)

        count = 0
        for i in range(width):
            if final_binary_value[i] != binary_k[i]:
                count += 1

        return count
