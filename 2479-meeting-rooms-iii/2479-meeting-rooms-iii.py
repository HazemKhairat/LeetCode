class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        cnt = [0] * n
        available = [0] * n

        def assign(start, end):
            minTime = inf
            minIdx = 0
            found = False
            for i in range(n):
                if available[i] <= start:
                    found = True
                    cnt[i] += 1
                    available[i] = end
                    break

                if minTime > available[i]:
                    minTime = available[i]
                    minIdx = i

            if not found:
                available[minIdx] += end - start
                cnt[minIdx] += 1

        for [start, end] in meetings:
            assign(start, end)

        value = 0
        room = 0
        for i in range(n):
            if value < cnt[i]:
                value = cnt[i]
                room = i

        return room
