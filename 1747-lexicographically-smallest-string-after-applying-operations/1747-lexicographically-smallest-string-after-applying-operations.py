class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        tmp = []
        for ch in s:
            tmp.append(int(ch))
        ans = tmp.copy()
        q = deque()
        q.append(ans)
        n = len(s)
        vis = set()

        while q:
            root = q.popleft()
            ans = min(ans, root)
            newS = root.copy()
            for i in range(n, 2):
                newS[i] = (root[i] + a) % 10

            if tuple(newS) not in vis:
                q.append(newS)
                vis.add(tuple(newS))
            newS = root.copy()
            for i in range(1, n, 2):
                newS[i] = (root[i] + a) % 10

            if tuple(newS) not in vis:
                q.append(newS)
                vis.add(tuple(newS))

            newS = root[b:] + root[:b]
            if tuple(newS) not in vis:
                q.append(newS)
                vis.add(tuple(newS))

        for i in range(len(ans)):
            ans[i] = str(ans[i])

        return "".join(ans)
