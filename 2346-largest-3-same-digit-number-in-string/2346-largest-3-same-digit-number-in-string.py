class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i, j, k = 0, 1, 2
        ans = ""
        while k < len(num):
            if num[i] == num[j] == num[k]:
                ans = max(ans, num[i:k+1])
            i += 1
            j += 1
            k += 1
            
        return ans
