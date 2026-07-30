class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = 0
        x = 1
        ans = 0
        for i in range(len(word)):
            cnt += 1
            ans += x
            if cnt == 8:
                cnt = 0
                x += 1
            

        return ans
                