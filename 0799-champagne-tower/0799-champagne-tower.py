class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        tower = [[0] * 101 for _ in range(101)]
        tower[0][0] = poured

        for r in range(query_row + 1):
            for c in range(query_row + 1):
                if tower[r][c] > 1:
                    exceed = (tower[r][c] - 1.0) / 2.0
                    tower[r][c] = 1
                    tower[r + 1][c] += exceed
                    tower[r + 1][c + 1] += exceed

        return tower[query_row][query_glass]
