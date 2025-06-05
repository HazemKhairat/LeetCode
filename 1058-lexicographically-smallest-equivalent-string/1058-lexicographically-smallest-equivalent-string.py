class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        ch = "a"

        while True:
            parent[ch] = ch
            if ch == "z":
                break
            ch = chr(ord(ch) + 1)

        def find(char):
            if parent[char] != char:
                parent[char] = find(parent[char])
            return parent[char]

        def union(str1, str2):
            a = find(str1)
            b = find(str2)

            if a == b:
                return

            if a < b:
                parent[b] = a
            elif b < a:
                parent[a] = b
            else:
                parent[a] = b

        for i in range(len(s1)):
            union(s1[i], s2[i])

        res = ""

        for ch in baseStr:
            res += find(ch)
        return res
