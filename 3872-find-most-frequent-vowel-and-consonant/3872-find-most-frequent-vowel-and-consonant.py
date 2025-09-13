class Solution:
    def maxFreqSum(self, s: str) -> int:
        vols = Counter()
        cons = Counter()

        for ch in s: 
            if ch in "aeiou":
                vols[ch] += 1
            else:
                cons[ch] += 1
                
        f =   max(vols.values()) if vols else 0
        s = max(cons.values()) if cons else 0

        return f + s