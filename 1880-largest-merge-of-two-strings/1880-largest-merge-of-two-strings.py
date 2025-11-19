class Solution:
    def largestMerge(self, str1: str, str2: str) -> str:
        ans = ""
        while str1 and str2:
            if str1 > str2:
                ans += str1[0]
                str1 = str1[1:]
            else:
                ans += str2[0]
                str2 = str2[1:]
            
        return ans + str1 + str2
