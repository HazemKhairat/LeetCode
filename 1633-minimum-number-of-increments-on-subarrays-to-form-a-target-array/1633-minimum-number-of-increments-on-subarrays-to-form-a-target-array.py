class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        res = prev = target[0]
        for i in range(1, n):
            if target[i] - prev > 0:
                res += target[i] - prev
            prev = target[i]
        return res
