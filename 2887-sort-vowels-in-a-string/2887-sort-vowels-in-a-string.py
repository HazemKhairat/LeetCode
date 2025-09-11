class Solution:
    def sortVowels(self, s: str) -> str:
        
        s = list(s)

        t = [''] * len(s)
        vols = []
        for i, ch in enumerate(s):
            if ch.lower() in "aeiou":
                vols.append(ch)
            else:
                t[i] = ch
        
        vols.sort()
        j = 0
        for i in range(len(s)):
            if t[i] == '':
                t[i] = vols[j]
                j += 1

        return ''.join(t)