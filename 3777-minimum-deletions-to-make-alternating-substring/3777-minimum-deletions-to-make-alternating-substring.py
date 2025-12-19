class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def add(self, i, val):
        while i < len(self.tree):
            self.tree[i] += val
            i += i & (-i)

    def query(self, i):
        pref = 0
        while i > 0:
            pref += self.tree[i]
            i -= i & (-i)
        return pref


class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        A = [ord(ch) - ord("A") for ch in s]

        bit = FenwickTree(n)

        for i in range(n - 1):
            if A[i] == A[i + 1]:
                bit.add(i + 1, 1)

        ans = []
        for q in queries:

            if q[0] == 1:
                i = q[1]
                A[i] ^= 1
                if i > 0:
                    bit.add(i, 1 if A[i] == A[i - 1] else -1)
                if i < n - 1:
                    bit.add(i + 1, 1 if A[i] == A[i + 1] else -1)
            else:
                l, r = q[1], q[2]
                ans.append(bit.query(r) - bit.query(l))

        return ans
