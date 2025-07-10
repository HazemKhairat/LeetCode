class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        arr = []
        arr.append((startTime[0] - 0, 0))
        for i in range(1, len(startTime)):
            arr.append((startTime[i] - endTime[i - 1], i))
        arr.append((eventTime - endTime[-1], len(startTime)))

        # get max Three spacess with indexes
        maxThree = sorted(arr)
        maxThree = maxThree[len(arr) - 3:]

        # loop and compare each event with max spaces in order 
        res = -1
        for i in range(len(startTime)):
            eventSize = endTime[i] - startTime[i]
            currSpace = arr[i][0] + arr[i + 1][0]
            idx1, idx2 = arr[i][1], arr[i + 1][1]
            j = len(maxThree) - 1
            while j >= 0 and (idx1 == maxThree[j][1] or idx2 == maxThree[j][1]):
                j -= 1
            
            if j >= 0 and eventSize <= maxThree[j][0]:
                res = max(res, currSpace + eventSize)
            else:
                res = max(res, currSpace)

        return res