from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.append(target)
        set_of_letters = set(letters)
        list_of_set = list(set_of_letters)
        list_of_set.sort()

        # list_of_set.append(target)
        # list_of_set.sort()

        if (list_of_set.index(target) + 1) == len(list_of_set):
            return list_of_set[0]

        index = list_of_set.index(target)

        # print("index", index)
        # print("list_of_set", list_of_set)

        return list_of_set[index + 1]