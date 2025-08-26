class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        
        ans = 0
        maxi = 0
        for l, w in dimensions:
            dig = math.sqrt((l**2 + w**2))
            if dig > maxi:
                maxi = dig
                ans = l * w
            elif dig == maxi:
                ans = max(ans, l * w)
        return ans