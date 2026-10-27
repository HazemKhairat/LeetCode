class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        grid.append("." * n)
        for i in range(1, m):
            row = "#" * (n - 1) + "."
            grid.append(row)

        return grid
