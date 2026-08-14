class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        i, j = 0, 0
        cnt = Counter()
        ans = 0
        while j < len(s):
            cnt[s[j]] += 1
            while cnt[s[j]] > 2:
                cnt[s[i]] -= 1
                i += 1
            j += 1
            ans= max(ans, j - i)
            
        return ans
                