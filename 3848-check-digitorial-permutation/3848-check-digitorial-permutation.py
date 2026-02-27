class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        fact = [1] * 10
        for i in range(1, 10):
            fact[i] = i * fact[i - 1]

        cnt1 = [0] * 10
        s_n = str(n)
        res = 0
        for ch in s_n:
            d = int(ch)
            cnt1[d] += 1
            res += fact[d]

        s_res = str(res)
        if len(s_n) != len(s_res):
            return False

        cnt2 = [0] * 10
        for ch in s_res:
            d = int(ch)
            cnt2[d] += 1

        return cnt1 == cnt2
