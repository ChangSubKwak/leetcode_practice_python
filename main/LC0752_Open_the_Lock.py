from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1

        queue = deque([("0000", 0)])
        visited = set("0000")

        while queue:
            current, count = queue.popleft()

            if current == target:
                return count

            for i in range(4):
                for delta in [-1, 1]:
                    new_digit = (int(current[i]) + delta) % 10
                    new = (current[:i] + str(new_digit) + current[i + 1:])

                    if new not in visited and new not in deadends:
                        visited.add(new)
                        queue.append((new, count + 1))

        return -1

