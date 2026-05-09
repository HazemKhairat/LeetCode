class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        n, m = len(grid), len(grid[0])

        layers = defaultdict(list)
        l1, l2 = n, m
        row = col = 0
        while row < (n // 2) and col < (m // 2):
            arr = []

            r, c = row, col
            for i in range(c, l2):
                arr.append([r, i])
            c = l2 - 1

            for i in range(r + 1, l1):
                arr.append([i, c])
            r = l1 - 1

            for i in range(c - 1, col - 1, -1):
                arr.append([r, i])
            c = col

            for i in range(r - 1, row, -1):
                arr.append([i, c])
            r = row

            layers[row] = arr
            row += 1
            col += 1
            l1 -= 1
            l2 -= 1

        ans = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(len(layers)):
            MOD = len(layers[i])
            shift = k % MOD
            for j in range(len(layers[i])):
                r1, c1 = layers[i][j]
                r2, c2 = layers[i][(j + shift) % MOD]
                ans[r1][c1] = grid[r2][c2]

        return ans
