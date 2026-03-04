class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        n, m = len(mat), len(mat[0])
        ans = 0
        r_cnt = [0] * n
        c_cnt = [0] * m

        for r in range(n):
            for c in range(m):
                r_cnt[r] += mat[r][c]
                c_cnt[c] += mat[r][c]

        for r in range(n):
            for c in range(m):
                if mat[r][c] == 1:
                    ans += r_cnt[r] == c_cnt[c] == 1

        return ans
