class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        def isSorted(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True

        def findMinPair(arr):
            mini = inf
            fIdx, sIdx = -1, -1
            for i in range(1, len(arr)):
                if arr[i] + arr[i - 1] < mini:
                    mini = arr[i] + arr[i - 1]
                    fIdx, sIdx = i - 1, i
            return (fIdx, sIdx)

        def merge(idx, val, arr):
            return arr[:idx] + [val] + arr[idx + 2 :]

        arr = nums[::]
        ans = 0
        while not isSorted(arr):
            fIdx, sIdx = findMinPair(arr)
            val = arr[fIdx] + arr[sIdx]
            arr = merge(fIdx, val, arr)
            ans += 1

        return ans
