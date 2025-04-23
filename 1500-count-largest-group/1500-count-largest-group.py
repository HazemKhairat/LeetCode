class Solution:
    def countLargestGroup(self, n: int) -> int:

        cnt = Counter()
        largestSum = 0
        for i in range(1, n + 1):
            tmp = i
            sum = 0
            while tmp:
                sum += tmp % 10
                tmp //= 10
            cnt[sum] += 1
            largestSum = max(largestSum, cnt[sum])

        res = 0
        for num, sum in cnt.items():
            if sum == largestSum:
                res += 1
        return res
