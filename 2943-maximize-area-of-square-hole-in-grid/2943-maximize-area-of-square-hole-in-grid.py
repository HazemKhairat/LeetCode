class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, h: List[int], v: List[int]) -> int:
        h.sort()
        v.sort()
        i = 1
        hl = 1
        while i < len(h):
            tmp = 1
            while i < len(h) and h[i] == h[i - 1] + 1:
                tmp += 1
                i += 1
            hl = max(hl, tmp)
            i += 1
        
        i = 1
        vl = 1
        while i < len(v):
            tmp = 1
            while i < len(v) and v[i] == v[i - 1] + 1:
                tmp += 1
                i += 1
            vl = max(vl, tmp)
            i += 1
        
        l = min(hl, vl) + 1

        return l * l
