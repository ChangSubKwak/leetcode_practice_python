from typing import List


class LC1897_Redistribute_Characters_to_Make_All_Strings_Equal:
    def makeEqual(self, words: List[str]) -> bool:
        count = [0] * 26
        for word in words:
            for char in list(word):
                count[ord(char) - ord("a")] += 1

        for i in range(26):
            if count[i] % len(words) != 0:
                return False

        return True