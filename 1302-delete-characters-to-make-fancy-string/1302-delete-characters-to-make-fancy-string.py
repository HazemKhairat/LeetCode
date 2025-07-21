class Solution:
    def makeFancyString(self, s: str) -> str:
        
        prev = s[0] # a
        freq = 1
        ans = s[0] # aabaa

        for i in range(1, len(s)):
            if s[i] == prev: # a , a
                freq += 1 # 4
            else:
                prev = s[i]
                freq = 1
            
            if freq < 3:
                ans += s[i]
            
        return ans

