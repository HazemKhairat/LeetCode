class Solution:
    def countDistinct(self, n: int) -> int:
        s = str(n)
        m = len(s)

        powOf9 = [1] * (m + 1)
        ans = 0
        for i in range(1, m):
            powOf9[i] = powOf9[i - 1] * 9
            ans += powOf9[i]

        i = 0
        while i < m:
            if s[i] == "0":
                break
            digit = int(s[i])
            ans += (digit - 1) * (powOf9[m - i - 1])
            i += 1

        return ans + 1 if i == m else ans
