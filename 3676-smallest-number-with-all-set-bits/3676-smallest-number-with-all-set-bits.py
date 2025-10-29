class Solution:
    def smallestNumber(self, n: int) -> int:

        while True:
            tmp = n
            ok = True
            while tmp:
                if not (tmp & 1):
                    ok = False
                    break
                tmp //= 2
            if ok:
                return n
            n += 1

        return n
