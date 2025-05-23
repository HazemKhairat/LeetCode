class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = []  # stores first item and index of each interval

        for i in range(n):
            arr.append([intervals[i][0], i])
        arr.sort()

        # implement lower_bound
        res = []
        for i in range(n):
            # r should be n not n - 1 to ensure that l reach the last index.
            l, r = 0, n
            while l < r: # because r = mid not mid - 1
                mid = (l + r) // 2
                if arr[mid][0] >= intervals[i][1]:
                    r = mid
                else:
                    l = mid + 1
            x = -1
            if l < n:
                x = arr[l][1]

            res.append(x)

        return res
