class Solution:
    def xorAfterQueries(self, A: List[int], q: List[List[int]]) -> int:
        MOD = 10**9 + 7

        for l, r, k, v in q:
            idx = l

            while idx <= r:
                A[idx] = ((A[idx] * v) % MOD )
                idx += k

        ans = 0

        for num in A:
            ans ^= num

        return ans