class Solution:
    def isTrionic(self, n: List[int]) -> bool:

        for p in range(1, len(n) - 2):
            inc = all(n[i] < n[i + 1] for i in range(p))
            if not inc:
                continue
            for q in range(p + 1, len(n) - 1):
                dec = all(n[i] > n[i + 1] for i in range(p, q))

                if not dec:
                    continue

                inc2 = all(n[i] < n[i + 1] for i in range(q, len(n) - 1))

                if inc2:
                    return True

        return False
            