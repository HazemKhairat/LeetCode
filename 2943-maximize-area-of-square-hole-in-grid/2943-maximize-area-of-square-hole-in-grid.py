class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, h: List[int], v: List[int]) -> int:
        h.sort()
        v.sort()

        def solve(arr):
            i = 0
            res = 1
            while i < len(arr) - 1:
                tmp = 1
                while i < len(arr) - 1 and arr[i] + 1 == arr[i + 1]:
                    tmp += 1
                    i += 1
                res = max(res, tmp)
                i += 1
            return res

        return (min(solve(h), solve(v)) + 1) ** 2
