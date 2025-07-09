class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        window = k + 1

        arr = []
        arr.append(0)
        arr.append(startTime[0] - 0)

        for i in range(1, len(startTime)):
            arr.append(startTime[i] - endTime[i - 1])
        arr.append(eventTime - endTime[-1])

        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]

        res = 0

        left, right = 0, window

        while right < len(arr):
            res = max(res, arr[right] - arr[left])
            left += 1
            right += 1
        
        return res


        
        



