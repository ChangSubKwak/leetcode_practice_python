from typing import List


class LC1662_Check_If_Two_String_Arrays_are_Equivalent:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        completed1 = ""
        for word in word1:
            completed1 += word

        completed2 = ""
        for word in word2:
            completed2 += word

        return completed1 == completed2
