class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDig = set()
        negDig = set()

        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for col in range(n):
                if col in cols or (row - col) in negDig or (row + col) in posDig:
                    continue

                cols.add(col)
                negDig.add(row - col)
                posDig.add(row + col)
                board[row][col] = "Q"

                backtrack(row + 1)

                cols.remove(col)
                negDig.remove(row - col)
                posDig.remove(row + col)
                board[row][col] = "."

        backtrack(0)
        return res
