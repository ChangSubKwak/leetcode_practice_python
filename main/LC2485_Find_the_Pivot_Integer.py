class Solution:
    def pivotInteger(self, n: int) -> int:
        forwardSumList = [0] * n
        reverseSumList = [0] * n

        forwardSum = 0
        reverseSum = 0
        for i in range(n):
            forwardSum += i + 1
            reverseSum += n - i
            forwardSumList[i] = forwardSum
            reverseSumList[n - i - 1] = reverseSum

        for i in range(n):
            if forwardSumList[i] == reverseSumList[i]:
                return i + 1

        return -1

