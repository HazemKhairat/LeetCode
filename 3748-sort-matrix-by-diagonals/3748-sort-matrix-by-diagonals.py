class Solution:
    def sortMatrix(self, g: List[List[int]]) -> List[List[int]]:
        n = len(g)
        for i in range(n):
            r = i
            c = 0
            arr = []
            while r < n:
                arr.append(g[r][c])
                r += 1
                c += 1
            r = i
            c = 0

            arr.sort()
            
            while r < n:
                g[r][c] = arr[-1]
                arr.pop()
                r += 1
                c += 1


        for i in range(1, n):
            r = 0
            c = i
            arr = []
            while c < n:
                arr.append(g[r][c])
                r += 1
                c += 1
            r = 0
            c = i
            arr.sort(reverse=True)
            while c < n:
                g[r][c] = arr[-1]
                arr.pop()
                r += 1
                c += 1

        return g
            