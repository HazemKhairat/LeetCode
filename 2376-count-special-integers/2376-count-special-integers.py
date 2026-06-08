class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        digits = [int(ch) for ch in s]

        dp = [
            [[[-1 for _ in range(1024)] for _ in range(2)] for _ in range(2)]
            for idx in range(10)
        ]

        def solve(idx, tight, started, mask):  # 10 , 2, 2, 1024

            if idx == len(digits):
                return 1 if started else 0

            if dp[idx][tight][started][mask] != -1:
                return dp[idx][tight][started][mask]

            k = digits[idx] if tight else 9
            res = 0

            for i in range(k + 1):
                newStarted = started or (i != 0)
                newTight = tight and (i == digits[idx])

                if not newStarted:
                    res += solve(idx + 1, newTight, False, mask)
                else:
                    if mask & (1 << i):
                        continue

                    res += solve(
                        idx + 1,
                        newTight,
                        newStarted,
                        mask | (1 << i),
                    )
                    
            dp[idx][tight][started][mask] = res
            return res

        return solve(0, 1, False, 0)
