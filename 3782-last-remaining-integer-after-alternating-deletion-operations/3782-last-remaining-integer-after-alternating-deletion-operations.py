class Solution:
    def lastInteger(self, n: int) -> int:
 
        start, step, leftToRght = 1, 1, True  

        while n > 1:                                
            if n%2 == 0:
                if not leftToRght: 
                    start += step
            step*= 2
            n = (n+1)//2
            leftToRght^= True

        return start                                 