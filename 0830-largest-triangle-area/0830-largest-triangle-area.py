class Solution:
    def largestTriangleArea(self, p: List[List[int]]) -> float:
        
        ans = 0
        n = len(p)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a, b, c = dist(p[i], p[j]), dist(p[j], p[k]), dist(p[i], p[k])
                    s = (a + b + c) / 2
                    area = sqrt( max(0, s * (s - a) * (s - b) * (s - c) ))
                    ans = max(ans, area)
        
        return ans