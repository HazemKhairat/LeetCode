class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        arr = [0] * (n + 1)

        for query in queries:
            x, y = query[0], query[1]
            arr[x] += -1
            arr[y + 1] += 1

        for i in range(1, n + 1):
            arr[i] += arr[i - 1]

        print(arr)

        for i in range(n):
            if nums[i] + arr[i] > 0:
                return False
        return True
