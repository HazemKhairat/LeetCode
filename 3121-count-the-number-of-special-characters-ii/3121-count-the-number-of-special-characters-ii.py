class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        last_idx = Counter()
        first_idx = Counter()
        for i in range(len(word) - 1, -1, -1):
            ch = word[i]
            if ch.isupper():
                first_idx[ch] = i
                
        lowers = set()
        for i in range(len(word)):
            ch = word[i]
            if ch.islower():
                lowers.add(ch)
                last_idx[ch] = i
                
        uppers = set()
        
        for i in range(len(word)):
            ch = word[i]
            if ch.isupper() and last_idx[ch.lower()] < first_idx[ch] :
                uppers.add(ch)

        ans = 0
        for ch in lowers:
            if ch.upper() in uppers:
                ans += 1

        return ans
            