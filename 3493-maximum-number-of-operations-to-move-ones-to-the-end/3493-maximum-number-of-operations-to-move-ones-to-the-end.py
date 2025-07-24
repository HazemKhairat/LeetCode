class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        res = 0
        
        for i in range(len(s) - 1):
            if s[i] == '1' and s[i + 1] == '0':
                ones += 1
                res += ones
            elif s[i] == '1':
                ones += 1

        return res
            