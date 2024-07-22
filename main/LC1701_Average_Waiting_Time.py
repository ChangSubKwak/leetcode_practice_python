from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = customers[0][0] + customers[0][1]
        average = current_time - customers[0][0]

        if len(customers) <= 1:
            return average

        i = 1
        while i < len(customers):
            if current_time < customers[i][0]:
                current_time = customers[i][0] + customers[i][1]
            else:
                current_time += customers[i][1]

            average += current_time - customers[i][0]
            i += 1

        return average / len(customers)

