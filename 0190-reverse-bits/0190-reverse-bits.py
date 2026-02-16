class Solution:
    def reverseBits(self, n: int) -> int:

        def helper(n):
            res = [0] * 32
            i = 0
            while n:
                res[i] = n % 2
                n //= 2
                i += 1
            return res[::-1]

        bits = helper(n)
        ans = 0
        for i in range(len(bits)):
            ans += (2**i) * bits[i]
            
        return ans
