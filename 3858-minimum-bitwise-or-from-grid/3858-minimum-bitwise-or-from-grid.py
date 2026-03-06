class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        res = (1 << 18) - 1

        for bit in range(17, -1, -1):
            curr = res & ~(1 << bit)
            ok = True
            for row in grid:
                if not any((n | curr) == curr for n in row):
                    ok = False
                    break
                
            if ok:
                res = curr
        return res


