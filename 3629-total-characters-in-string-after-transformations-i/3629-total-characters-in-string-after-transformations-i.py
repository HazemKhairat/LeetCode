class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        curr = [0] * 26
        MOD = 10**9 + 7

        for ch in s:
            curr[ord(ch) - ord("a")] += 1

        for i in range(t):
            next = [0] * 26
            for j in range(len(curr)):
                if curr[j]:
                    if j < 25:
                        next[j + 1] = curr[j]
                    else:
                        next[0] += curr[j]
                        next[1] += curr[j]
            curr = next

        res = sum(curr)
        return res % MOD
