class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        cnt = Counter()
        n = len(s)
        left, right = 0, 0
        res = 0
        while right < n:
            cnt[s[right]] += 1
            while cnt[s[right]] >= k:
                res += n - right
                cnt[s[left]] -= 1
                left += 1             
                
            right += 1
                
        return res
            