class Solution:
    def findComplement(self, num: int) -> int:
        binary_num = ""
        original_num = num

        while num >= 1:
            binary_num = str(int(num % 2)) + binary_num
            num /= 2

        complement_binary_num = ""
        for digit in list(binary_num):
            complement_binary_num += ("1" if digit == "0" else "0")

        result = 0
        length = len(complement_binary_num)

        for i in range(length):
            result += pow(2, length - i - 1) * int(complement_binary_num[i])

        return result
