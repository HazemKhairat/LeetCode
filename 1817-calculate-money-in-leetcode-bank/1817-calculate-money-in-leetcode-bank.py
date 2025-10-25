class Solution:
    def totalMoney(self, n: int) -> int:
        start = 1
        curr = start
        ans = 0
        week = 1

        for i in range(n):
            ans += curr
            curr += 1
            if week == 7:
                week = 0
                start += 1
                curr = start
            week += 1

        return ans
