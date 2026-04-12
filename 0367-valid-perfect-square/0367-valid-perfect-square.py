class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        l, r = 1, num
        
        while l <= r:
            mid = (l + r) // 2
            val = mid * mid
            if val == num:
                return True
            elif val > num:
                r = mid - 1
            else:
                l = mid + 1
        
        return False