class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        l2 = math.ceil(l ** (1 / k))
        r2 = math.ceil(r ** (1 / k))

        return r2 - l2 + 1 if r2 ** k == r else r2 - l2
