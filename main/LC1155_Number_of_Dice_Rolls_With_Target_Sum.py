class LC1155_Number_of_Dice_Rolls_With_Target_Sum:
    def __init__(self):
        self.dp = [[0 for _ in range(1001)] for _ in range(31)]

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n == 0 or target <= 0:
            return 1 if n == 0 and target == 0 else 0

        if self.dp[n][target] != 0:
            return self.dp[n][target] - 1

        count = 0
        for i in range(1, k + 1):
            count = (count + self.numRollsToTarget(n - 1, k, target - i)) % 1000000007

        self.dp[n][target] = count + 1

        return count
