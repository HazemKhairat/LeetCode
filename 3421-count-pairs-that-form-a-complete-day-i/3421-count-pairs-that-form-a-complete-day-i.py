class Solution:
    def countCompleteDayPairs(self, h: List[int]) -> int:
        n = len(h)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (h[i] + h[j]) % 24 == 0:
                    ans += 1
        return ans