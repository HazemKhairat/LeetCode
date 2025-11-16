class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        n = len(s1)
        for i in range(n):
            parent[s1[i]] = s1[i]
            parent[s2[i]] = s2[i]

        def find(ch):
            if parent[ch] == ch:
                return ch
            parent[ch] = find(parent[ch])
            return parent[ch]

        def union(ch1, ch2):
            p1, p2 = find(ch1), find(ch2)
            if p1 == p2:
                return

            if p1 < p2:
                parent[p2] = p1
            else:
                parent[p1] = p2

        for i in range(n):
            union(s1[i], s2[i])

        ans = ""
        for ch in baseStr:
            if ch in parent:
                ans += find(ch)
            else:
                ans += ch

        return ans
