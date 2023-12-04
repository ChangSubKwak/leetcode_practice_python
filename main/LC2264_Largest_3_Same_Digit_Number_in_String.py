class LC2264_Largest_3_Same_Digit_Number_in_String:
    def isSameThree(self, num: str) -> bool:
        return num[0] == num[1] and num[1] == num[2]


    def largestGoodInteger(self, num: str) -> str:
        max = ""
        for i in range(len(num) - 2):
            part = num[i:i+3]
            if self.isSameThree(part):
                if max == "" or max <= part:
                    max = part

        return max

