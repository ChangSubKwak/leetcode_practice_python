from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        print("people", people)

        count = 0
        weight_sum = 0
        length = len(people)

        left = 0
        right = length - 1

        weight_sum = people[left]
        weight_add_count = 1

        while left <= right:
            if weight_add_count == 2:
                left += 1
                count += 1

                if left < length:
                    weight_sum = people[left]
                    weight_add_count = 1

                # print("1 - left", left, "right", right, "weight_sum", weight_sum, "weight_add_count", weight_add_count, "count", count)
                continue

            if weight_sum == limit:
                left += 1
                count += 1
                weight_sum = people[left]
                weight_add_count = 1
                # print("2 - left", left, "right", right, "weight_sum", weight_sum, "weight_add_count", weight_add_count, "count", count)
                continue

            if weight_sum + people[right] < limit:
                if left == right:
                    right -= 1
                    count += 1
                    continue

                weight_sum += people[right]
                weight_add_count += 1
                right -= 1
                # print("3 - left", left, "right", right, "weight_sum", weight_sum, "weight_add_count", weight_add_count, "count", count)
                continue

            if weight_sum + people[right] > limit:
                left += 1
                count += 1

                if left < length:
                    weight_sum = people[left]
                else:
                    weight_sum = 0
                weight_add_count = 1

                # print("4 - left", left, "right", right, "weight_sum", weight_sum, "weight_add_count", weight_add_count, "count", count)
                continue

            if weight_sum + people[right] == limit:
                right -= 1
                left += 1
                count += 1

                if left < length:
                    weight_sum = people[left]
                    weight_add_count = 1

                # print("5 - left", left, "right", right, "weight_sum", weight_sum, "weight_add_count", weight_add_count, "count", count)

        # print("6 - left", left, "right", right, "weight_sum", weight_sum, "count", count)

        return count