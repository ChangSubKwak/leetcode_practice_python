from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for operation in operations:
            if "--" in operation:
                count -= 1
                # continue

            if "++" in operation:
                count += 1

            print(operation, count)

        return count