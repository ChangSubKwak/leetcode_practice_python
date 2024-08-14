from typing import List
import copy

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()
        self.recur(candidates, target, 0, [], answer)

        return answer

    def recur(self, candidates, target, start_index, current, answer):
        if target < 0:
            return

        if target == 0:
            answer.append(copy.deepcopy(current))

        for i in range(start_index, len(candidates)):
            if i > start_index and candidates[i] == candidates[i - 1]:
                continue

            current.append(candidates[i])
            self.recur(candidates, target - candidates[i], i + 1, current, answer)
            del current[-1]
