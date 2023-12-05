class LC1688_Count_of_Matches_in_Tournament:
    def numberOfMatches(self, n: int) -> int:
        matchCount = 0
        while n >= 2:
            if n % 2 == 0:
                matchCount += n / 2
                n /= 2
            else:
                matchCount += (n - 1) / 2
                n = (n - 1) / 2 + 1

        return int(matchCount)