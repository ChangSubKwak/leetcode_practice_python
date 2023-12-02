from typing import List


class LC1160_Find_Words_That_Can_Be_Formed_by_Characters:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = {}
        for i in range(26):
            count[chr(ord('a') + i)] = 0

        for c in chars:
            count[c] += 1

        result = 0
        for word in words:
            copy_count = count.copy()
            isMatch = True
            for c in word:
                copy_count[c] -= 1
                if copy_count[c] < 0:
                    isMatch = False
                    break

            if isMatch:
                result += len(word)

        return result
