class LC1758_Minimum_Changes_To_Make_Alternating_Binary_String:
    def minOperations(self, s: str) -> int:
        length = len(s)

        count1 = 0
        count2 = 0

        for i in range(length):
            if i % 2 == 0:
                if s[i] == '1':
                    count1 += 1
                elif s[i] == '0':
                    count2 += 1
            else:
                if s[i] == '0':
                    count1 += 1
                elif s[i] == '1':
                    count2 += 1

        return min(count1, count2)
