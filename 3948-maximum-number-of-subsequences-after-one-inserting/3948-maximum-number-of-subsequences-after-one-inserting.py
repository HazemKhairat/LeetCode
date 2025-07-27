class Solution:
    def numOfSubsequences(self, s: str) -> int:
        n = len(s)
        prefL = [0] * (n + 1)
        suffT = [0] * (n + 1)

        for i in range(1, n):
            if s[i - 1] == 'L':
                prefL[i] = 1
            prefL[i] += prefL[i - 1]
        
        for i in range(n - 1, -1, -1):
            if s[i] == 'T':
                suffT[i] = 1
            suffT[i] += suffT[i + 1]
            

        l, c, t, bestPosForC = 0, 0, 0, 0
        for i in range(n):
            if s[i] == 'C':
                c += prefL[i] * suffT[i]
                l += (prefL[i] + 1) * suffT[i]
                t += prefL[i] * (suffT[i] + 1)
            else:
                bestPosForC = max(bestPosForC, prefL[i] * suffT[i])

        c += bestPosForC

        return max(l, c, t)

