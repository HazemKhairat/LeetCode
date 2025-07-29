class Solution:
    def totalNumbers(self, d: List[int]) -> int:
        n = len(d)
        used = set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k:
                        continue
                    num = d[i] * 100 + d[j] * 10 + d[k]
                    if num >= 100 and num % 2 == 0:
                        used.add(num)
        return len(used)
                    