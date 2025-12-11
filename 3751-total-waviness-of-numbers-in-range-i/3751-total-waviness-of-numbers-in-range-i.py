class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        ans = 0
        for num in range(num1, num2 + 1):
            s = str(num)
            for i in range(1, len(s) - 1):
                prev, curr, nxt = int(s[i - 1]), int(s[i]), int(s[i + 1])
                if (prev < curr > nxt) or (prev > curr < nxt):
                    ans += 1

        return ans
            
            