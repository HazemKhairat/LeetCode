class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        ans = inf
        maxi = max(cnt.values())

        for i in range(1, maxi + 1):
            tmp = 0
            for freq in cnt.values():
                if freq < i:
                    tmp += freq
                elif freq > (i + k):
                    tmp += freq - (i + k)
            ans = min(ans, tmp)

        return ans
