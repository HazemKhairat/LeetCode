class Solution:
    def minMovesToCaptureTheQueen(
        self, a: int, b: int, c: int, d: int, e: int, f: int
    ) -> int:

        if a == e == c and min(b, f) < d < max(b, f):
            return 2
        elif a == e:
            return 1

        if b == f == d and min(a, e) < c < max(a, e):
            return 2
        elif b == f:
            return 1

        if abs(c - e) == abs(f - d):
            if abs(a - c) == abs(b - d) and min(c, e) < a < max(c, e) and min(d, f) < b < max(d, f):
                return 2
            return 1
    

        return 2
