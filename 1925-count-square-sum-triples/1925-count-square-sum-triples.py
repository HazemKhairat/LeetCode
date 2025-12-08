class Solution:
    def countTriples(self, n: int) -> int:
        ans =  0
        k = set([i * i for i in range(1, n + 1)])
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if (j * j) + (i * i) in k:
                    ans += 1
        return ans