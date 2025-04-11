class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # loop from 0 to n / 2
        # loop from n / 2 to n
        # make sum1, sum2 and compare
        # count number of valids

        count = 0
        for i in range(low, high + 1):
            s = str(i)
            n = len(s)
            if n % 2 == 1:
                continue
            sum1, sum2 = 0, 0
            for j in range(0, n // 2):
                sum1 = sum1 + int(s[j])
            for j in range(n // 2, n):
                sum2 = sum2 + int(s[j])

            if sum1 == sum2:
                count += 1
                
        return count
