class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd = 0
        if low % 2 == 0 and high % 2 == 0:
            odd = (high - low) // 2
        elif low % 2 == 1 and high % 2 == 1:
            odd = (high - low) // 2 + 1
        else:
            odd = (high - low) // 2  + 1
        
        return odd
        
