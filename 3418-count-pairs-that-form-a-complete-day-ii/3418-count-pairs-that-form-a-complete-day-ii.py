class Solution:
    def countCompleteDayPairs(self, h: List[int]) -> int:

        cnt = Counter()
        ans = 0
        for x in h:
            r = x % 24
            comp = (24 - r) % 24
            ans += cnt[comp]
            cnt[r] += 1
                            
        return ans

        
        