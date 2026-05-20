class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = [0] * n
        freq = [0] * (n + 1)
        pref = 0

        for i in range(n):
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                pref += 1

            freq[B[i]] += 1
            if freq[B[i]] == 2:
                pref += 1

            ans[i] = pref

        return ans
