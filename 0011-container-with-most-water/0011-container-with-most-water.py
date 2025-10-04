class Solution:
    def maxArea(self, h: List[int]) -> int:
        i, j = 0, len(h) - 1
        ans = 0
        while i < j:
            ans = max(ans, min(h[i], h[j]) * (j - i))
            if h[i] < h[j]:
                i += 1
            else:
                j -= 1
        
        return ans