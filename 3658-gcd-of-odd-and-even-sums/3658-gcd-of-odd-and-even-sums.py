class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        k = 0
        tmp = n
        while tmp:
            sumOdd += k + 1
            k += 2
            tmp -= 1

        sumEven = 0
        k = -1
        tmp = n
        while tmp:
            sumEven += k + 1
            k += 2
            tmp -= 1

        return math.gcd(sumOdd, sumEven)
        