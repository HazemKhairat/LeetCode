class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        cnt1 = Counter(words)
        print(cnt1)

        n = len(s)
        m = len(words[0])
        l, r = 0, (len(words) * len(words[0]))
        res = []
        while r <= n:
            cnt2 = Counter()
            i = l
            while i < r:
                cnt2[s[i:i + m]] += 1
                # print(s[i:i + m])
                i += m
            
            # print(cnt2)
            if cnt1 == cnt2:
                res.append(l)

            l += 1
            r += 1
        
        return res