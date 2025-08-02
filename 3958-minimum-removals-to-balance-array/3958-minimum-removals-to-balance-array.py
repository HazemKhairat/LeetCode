class Solution:
    def minRemoval(self, A: List[int], k: int) -> int:
        A.sort()
        n = len(A)
        res = inf

        def lower_bound_custom(i, target):
            left, right = 0, i + 1
            while left < right:
                mid = (left + right) // 2
                if A[mid] * k >= target:
                    right = mid
                else:
                    left = mid + 1
            return left if left <= i else -1

        res = inf
        for i in range(n - 1, -1, -1):
            l = lower_bound_custom(i, A[i])
            if l != -1:
                res = min(res, (n - i - 1) + l)

        return res if res != inf else 0
