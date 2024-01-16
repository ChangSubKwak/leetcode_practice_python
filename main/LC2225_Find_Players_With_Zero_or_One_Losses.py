from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        result = [[], []]
        winnerSet = set()
        loserSet = set()

        lostStat = {}
        for match in matches:
            winner = match[0]
            if winner not in winnerSet:
                winnerSet.add(winner)

            loser = match[1]
            if loser not in loserSet:
                loserSet.add(loser)

            if match[1] not in lostStat:
                lostStat[match[1]] = 0
            lostStat[match[1]] += 1

        for match in matches:
            loser = match[1]

            if loser in winnerSet:
                winnerSet.remove(loser)

        for winner in winnerSet:
            result[0].append(winner)

        for key, value in lostStat.items():
            if value == 1:
                result[1].append(key)

        result[0].sort()
        result[1].sort()

        return result