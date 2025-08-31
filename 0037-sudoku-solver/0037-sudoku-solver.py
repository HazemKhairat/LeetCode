class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        blocks = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                blocks[(r // 3) * 3 + (c // 3)].add(board[r][c])

        def backtrack(r, c):
            if r == 9:
                return True
            if c == 9:
                return backtrack(r + 1, 0)
            if board[r][c] != ".":
                return backtrack(r, c + 1)

            for k in range(1, 10):
                ch = str(k)
                idx = (r // 3) * 3 + (c // 3)
                if ch in rows[r] or ch in cols[c] or ch in blocks[idx]:
                    continue
                board[r][c] = ch
                rows[r].add(ch)
                cols[c].add(ch)
                blocks[idx].add(ch)
                if backtrack(r, c + 1):
                    return True
                board[r][c] = "."
                rows[r].remove(ch)
                cols[c].remove(ch)
                blocks[idx].remove(ch)

            return False

        backtrack(0, 0)
        return board
