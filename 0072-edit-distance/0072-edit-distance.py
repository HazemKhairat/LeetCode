class Solution:
    def helper(self, word1: str, word2: str, i, j, memo):
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j
        elif j == len(word2):
            return len(word1) - i
        elif word1[i] == word2[j]:
            return self.helper(word1, word2, i + 1, j + 1, memo)
        elif memo[i][j] != -1:
            return memo[i][j]
        insert = 1 + self.helper(word1, word2, i, j + 1, memo)
        delete = 1 + self.helper(word1, word2, i + 1, j, memo)
        replace = 1 + self.helper(word1, word2, i + 1, j + 1, memo)
        memo[i][j] = min(insert, delete, replace)
        return memo[i][j]

    def minDistance(self, word1: str, word2: str) -> int:
        n = max(len(word1), len(word2))
        memo = [[-1] * n for _ in range(n)]
        return self.helper(word1, word2, 0, 0, memo)
