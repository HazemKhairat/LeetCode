class MyCalendarThree:

    def __init__(self):
        self.pq = []
        self.cnt = Counter()
        self.maxi = 0


    def book(self, startTime: int, endTime: int) -> int:
        
        if startTime not in self.cnt:
            heapq.heappush(self.pq, startTime)
        if endTime not in self.cnt: 
            heapq.heappush(self.pq, endTime)

        self.cnt[startTime] += 1
        self.cnt[endTime] -= 1

        tmp = copy.deepcopy(self.pq)
        res = 0
        while tmp:
            time = heapq.heappop(tmp)
            res += self.cnt[time]
            self.maxi = max(res, self.maxi)
        
        return self.maxi



# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)