class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        while numBottles >= numExchange:
            divisor = numBottles // numExchange
            remainder = numBottles % numExchange

            result += divisor
            numBottles = divisor + remainder

        return result