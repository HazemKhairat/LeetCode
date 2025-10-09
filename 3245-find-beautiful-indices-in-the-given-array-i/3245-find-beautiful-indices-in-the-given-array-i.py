class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        A = SortedSet()
        B = SortedSet()

        for i in range(len(s) - len(a) + 1):
            if s[i : i + len(a)] == a:
                A.add(i)

        for j in range(len(s) - len(b) + 1):
            if s[j : j + len(b)] == b:
                B.add(j)

        ans = []

        for i in A:
            idx = B.bisect_left((i - k))
            if idx != len(B) and B[idx] <= i + k:
                ans.append(i)
        
        return ans
