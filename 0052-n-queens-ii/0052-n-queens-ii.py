class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        leftDig = set()  # r - c
        rightDig = set()  # r + c
        res = 0
        board = [["." for _ in range(n)] for _ in range(n)]

        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return

            for c in range(n):
                if c in cols or (r - c) in leftDig or (r + c) in rightDig:
                    continue

                board[r][c] = "Q"
                cols.add(c)
                leftDig.add(r - c)
                rightDig.add(r + c)

                backtrack(r + 1)

                board[r][c] = "."
                cols.remove(c)
                leftDig.remove(r - c)
                rightDig.remove(r + c)

        backtrack(0)
        return res
