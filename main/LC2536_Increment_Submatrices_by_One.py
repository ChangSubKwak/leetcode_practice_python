from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        answer = [[0] * n for _ in range(n)]

        for row1, col1, row2, col2 in queries:
            for i in range(row1, row2 + 1):
                answer[i][col1] += 1
                if col2 + 1 < n:
                    answer[i][col2 + 1] -= 1

        for y in range(n):
            for x in range(1, n):
                answer[y][x] += answer[y][x - 1]

        return answer
