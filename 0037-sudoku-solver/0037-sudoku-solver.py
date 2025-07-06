class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    rows[r].add(val)
                    cols[c].add(val)
                    squares[r // 3][c // 3].add(val)

        def backtrack(r, c):
            if r == 9:
                return True
            if c == 9:
                return backtrack(r + 1, 0)
            
            if board[r][c] != ".":
                return backtrack(r, c + 1)
            
            for i in range(1, 10):
                ch = str(i)
                if ch in rows[r] or ch in cols[c] or ch in squares[r // 3][c // 3]:
                    continue

                board[r][c] = ch
                rows[r].add(ch)
                cols[c].add(ch)
                squares[r // 3][c // 3].add(ch)

                if backtrack(r, c + 1):
                    return True

                board[r][c] = '.'
                rows[r].remove(ch)
                cols[c].remove(ch)
                squares[r // 3][c // 3].remove(ch)

            return False

        backtrack(0, 0)
        return board
        