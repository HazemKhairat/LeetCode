class Solution:
    def countOdds(self, l: int, h: int) -> int:
        return (h - l) // 2 if h % 2 == 0 and l % 2 == 0 else (h - l) // 2 + 1
        
