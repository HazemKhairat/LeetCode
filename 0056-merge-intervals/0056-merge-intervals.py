class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        lastInterval = intervals[0]
        n = len(intervals)
        i = 1
        ans = []

        while i < n:
            start, end = intervals[i]
            if end >= lastInterval[1] >= start:
                lastInterval[1] = end
            elif lastInterval[1] < start:
                ans.append(lastInterval)
                lastInterval = [start, end]

            i += 1

        ans.append(lastInterval)
        return ans
