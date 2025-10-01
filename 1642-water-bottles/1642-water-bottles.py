class Solution:
    def numWaterBottles(self, nb: int, ne: int) -> int:
        ans = 0
        em = 0
        while nb:
            ans += nb
            em += nb
            nb = em // ne
            em = em % ne
        
        return ans