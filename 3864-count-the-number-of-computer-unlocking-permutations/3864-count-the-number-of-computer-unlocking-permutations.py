MOD= 10**9 + 7

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        mini = min(complexity)

        if complexity[0] != mini:
            return 0

        if complexity.count(mini) > 1:
            return 0

        ans = 1

        for i in range(1, n):
            ans *= i
            ans %= MOD
            
        return ans
            