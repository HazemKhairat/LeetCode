class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = [0] * 26

        for ch in word:
            i = ord(ch) - 97
            cnt[i] += 1
            
        
        cnt = sorted(cnt, reverse=True)

        count = 0
        x = 1
        ans = 0
        for i in range(len(cnt)):
            count += 1
            ans += (cnt[i] * x)
            if count == 8:
                count = 0
                x += 1

        return ans