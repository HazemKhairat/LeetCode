class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n, m = len(mat), len(mat[0])

        pref = [[0] * (m + 1) for _ in range(n + 1)]

        for r in range(1, n + 1):
            for c in range(1, m + 1):
                pref[r][c] = (
                    mat[r - 1][c - 1]
                    + pref[r - 1][c]
                    + pref[r][c - 1]
                    - pref[r - 1][c - 1]
                )

        def getSum(r1, c1, r2, c2):
            return (
                pref[r2][c2]
                - pref[r2][c1 - 1]
                - pref[r1 - 1][c2]
                + pref[r1 - 1][c1 - 1]
            )

        minSide, ans = min(m, n), 0

        for r in range(1, n + 1):
            for c in range(1, m + 1):
                for k in range(ans + 1, minSide + 1):
                    r2, c2 = r + k - 1, c + k - 1
                    if r2 <= n and c2 <= m and getSum(r, c, r2, c2) <= threshold:
                        ans += 1
                    else:
                        break
        return ans
