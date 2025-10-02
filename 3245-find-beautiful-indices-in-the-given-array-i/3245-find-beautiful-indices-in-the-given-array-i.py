class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        A = SortedSet()
        B = SortedSet()
        for i in range(n - len(a) + 1):
            if s[i : i + len(a)] == a:
                A.add(i)

        for i in range(n - len(b) + 1):
            if s[i : i + len(b)] == b:
                B.add(i)
        # print(A)
        # print(B)
        ans = []
        for i in A:
            j = B.bisect_left(i - k)
            if j < len(B) and B[j] <= i + k:
                ans.append(i)

        return ans
