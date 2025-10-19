class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        ans = [int(ch) for ch in s]
        q = deque()
        q.append(ans)
        vis = set()

        while q:
            root = q.popleft()
            ans = min(ans, root)
            s1, s2 = root.copy(), (root[b:] + root[:b])

            for i in range(1, n, 2):
                s1[i] = (root[i] + a) % 10

            s1, s2 = tuple(s1), tuple(s2)

            for st in (s1, s2):
                if st not in vis:
                    q.append(list(st))
                    vis.add(st)

        ans = [str(ch) for ch in ans]
        return "".join(ans)
