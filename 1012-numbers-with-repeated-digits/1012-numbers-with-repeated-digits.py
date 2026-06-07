class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)
        digits = [int(ch) for ch in s]

        dp = [[[[[-1 for _ in range(1024)] for i in range(2)] for j in range(2)] for k in range(2)] for m in range(10)]

        def solve(idx, tight, repeated, started, mask):  # 10, 2, 2, 2, 1024
            if idx == len(digits):
                return 1 if repeated else 0

            if dp[idx][tight][repeated][started][mask] != -1:
                return dp[idx][tight][repeated][started][mask]

            k = digits[idx] if tight else 9
            res = 0

            for i in range(k + 1):
                newTight = tight if i == digits[idx] else 0
                newStarted = started or (i != 0)

                if not newStarted:
                    res += solve(idx + 1, newTight, repeated, False, mask)
                else:
                    res += solve(
                        idx + 1,
                        newTight,
                        repeated or ((mask & (1 << i)) != 0),
                        newStarted,
                        mask | (1 << i),
                    )

            dp[idx][tight][repeated][started][mask] = res
            return res

        return solve(0, 1, False, False, 0)
