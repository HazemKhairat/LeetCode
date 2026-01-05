class Solution:
    def maxMatrixSum(self, mat: List[List[int]]) -> int:
        mini = inf
        cnt = 0
        n = len(mat)
        ans = 0
        for i in range(n):
            for j in range(n):
                num = abs(mat[i][j])
                ans += num
                mini = min(mini, num)
                if mat[i][j] < 0:
                    cnt += 1

        return ans if cnt % 2 == 0 else ans - (mini * 2)
