from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        increase_dict = {}
        decrease_dict = {}

        length = len(rating)

        for i in range(length):
            for j in range(i + 1, length):
                if rating[i] < rating[j]:
                    increase_dict[i] = increase_dict.get(i, [])
                    increase_dict[i].append(j)

                if rating[i] > rating[j]:
                    decrease_dict[i] = decrease_dict.get(i, [])
                    decrease_dict[i].append(j)

        # print(increase_dict)
        # print(decrease_dict)

        total_count = 0
        for key, value in increase_dict.items():
            if len(increase_dict[key]) <= 1:
                continue

            for i in value:
                if i not in increase_dict:
                    continue
                total_count += len(increase_dict[i])

        for key, value in decrease_dict.items():
            if len(decrease_dict[key]) <= 1:
                continue

            for i in value:
                if i not in decrease_dict:
                    continue

                total_count += len(decrease_dict[i])

        return total_count
