class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        li = text.split()
        ans = 0
        
        for word in li:
            ok = True
            for ch in brokenLetters:
                if ch in word:
                    ok = False
                    break
            if ok: ans += 1
    
        return ans
