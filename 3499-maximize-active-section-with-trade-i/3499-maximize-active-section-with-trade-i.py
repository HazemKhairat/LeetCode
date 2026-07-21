class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        i = 0
        ones = sum(i == '1' for i in s)
        res = 0
        while i < n:
            if s[i] == '1':
                maxi = 0
                curr = i
                j = i
                while i < n and s[i] == '1':
                    i += 1

                block = i - j if j > 0 and s[j - 1] == '0' and i < n and s[i] == '0' else 0
                if j > 0 and s[j - 1] == '0' and i < n and s[i] == '0':
                    
                    left = j - 1
                    right = i
                    while left >= 0 and s[left] != '1':
                        left -= 1
                    left += 1
                    while right < n and s[right] != '1':
                        right += 1
                    # right -= 1
                    

                    maxi = (curr - left) + (right - curr)
                res = max(res, ones + maxi - block)
            else:
                i += 1
                    
        return res
            