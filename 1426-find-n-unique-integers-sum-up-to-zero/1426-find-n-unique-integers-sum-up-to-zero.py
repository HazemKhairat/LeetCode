class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        tmp = n // 2
        ans = []
        while tmp:
            ans.append(tmp)
            ans.append(-tmp)
            tmp -= 1
        
        if len(ans) != n: ans.append(0)
        return ans
