class Solution:
    def longestBalanced(self, s: str) -> int:

        n = len(s)
        ans = 1

        def isBalanced(arr):
            st = set()
            for i in range(len(arr)):
                if arr[i] != 0:
                    st.add(arr[i])
            return len(st) == 1

        for i in range(n):
            arr = [0] * 26
            for j in range(i, n):
                ch = ord(s[j]) - 97
                arr[ch] += 1
                if isBalanced(arr):
                    ans = max(ans, j - i + 1)

        return ans
