class Solution:
    def helper(self, s1: str, s2: str, i, j, memo):
        if i == len(s1) and j == len(s2):
            return 0
        elif i == len(s1):
            ascii_sum = sum(ord(ch) for ch in s2[j:])
            return ascii_sum
        elif j == len(s2):
            ascii_sum = sum(ord(ch) for ch in s1[i:])
            return ascii_sum
        elif s1[i] == s2[j]:
            return self.helper(s1, s2, i + 1, j + 1, memo)
        elif memo[i][j] != -1:
            return memo[i][j]
        deleteS1 = ord(s1[i]) + self.helper(s1, s2, i + 1, j, memo)
        deleteS2 = ord(s2[j]) + self.helper(s1, s2, i, j + 1, memo)
        memo[i][j] = min(deleteS1, deleteS2)
        return min(deleteS1, deleteS2)

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = max(len(s1), len(s2))
        memo = [[-1] * n for _ in range(n)]
        return self.helper(s1, s2, 0, 0, memo)
