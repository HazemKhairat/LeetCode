class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)

        @cache
        def solve(tmp, idx):
            if idx == n:
                return False
            ch = s[idx:idx+1]
            newWrod = False
            if (tmp + ch) in wordDict:
                if idx == n - 1: return True
                newWrod = solve("", idx + 1)
            ok = solve(tmp + ch, idx + 1)

            return ok or newWrod
            
            
        
        return solve("", 0)