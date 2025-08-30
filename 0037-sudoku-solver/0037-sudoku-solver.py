class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3) * 3 + c // 3].add(val)

        def solve(r, c):
            if r >= 9:
                return True
            if c >= 9:
                return solve(r + 1, 0)
            if board[r][c] != ".":
                return solve(r, c + 1)

            for k in range(1, 10):
                ch = str(k)
                box_idx = (r // 3) * 3 + c // 3
                if ch in rows[r] or ch in cols[c] or ch in boxes[box_idx]:
                    continue
                board[r][c] = ch
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[box_idx].add(ch)
                if solve(r, c + 1):
                    return True
                board[r][c] = "."
                rows[r].remove(ch)
                cols[c].remove(ch)
                boxes[(r // 3) * 3 + c // 3].remove(ch)

            return False

        solve(0, 0)
        return board
