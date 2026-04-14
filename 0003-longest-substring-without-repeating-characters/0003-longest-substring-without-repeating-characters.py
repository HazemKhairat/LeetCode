class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Handle edge case of length = 0
        if len(s) == 0:
            return 0

        # Define variables we need
        i, j, ans = 0, 1, 1
        n = len(s)
        mp = {}
        mp[s[0]] = 1

        while j < n:
            ch = s[j]
            mp[ch] = 1 if ch not in mp else mp[ch] + 1

            # Validation condition
            if mp[ch] > 1:
                while i < j and mp[ch] > 1:
                    mp[s[i]] -= 1
                    i += 1

            # Update answer
            ans = max(ans, j - i + 1)
            j += 1

        return ans
