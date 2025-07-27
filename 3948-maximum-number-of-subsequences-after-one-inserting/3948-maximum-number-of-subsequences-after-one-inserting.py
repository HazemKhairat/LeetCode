class Solution:
    def numOfSubsequences(self, s: str) -> int:
        n = len(s)
        prefix = [0] * (n + 1)  # `L` count (1-based)
        suffix = [0] * (n + 1)  # `T` count (0-based)

        for i in range(n):
            if s[i] == 'L':
                prefix[i + 1] = 1
            prefix[i + 1] += prefix[i]

        for i in range(n - 1, -1, -1):
            if s[i] == 'T':
                suffix[i] = 1
            suffix[i] += suffix[i + 1]

        resWithC = 0
        bestPosForC = 0
        resWithL = 0
        resWithT = 0

        for i in range(n):
            if s[i] == 'C':
                resWithC += prefix[i] * suffix[i]
                resWithL += (prefix[i] + 1) * suffix[i]
                resWithT += prefix[i] * (suffix[i] + 1)
            else:
                bestPosForC = max(bestPosForC, prefix[i] * suffix[i])

        resWithC += bestPosForC
        return max(resWithL, resWithT, resWithC)
