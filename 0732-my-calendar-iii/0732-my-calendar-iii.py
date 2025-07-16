class MyCalendarThree:

    def __init__(self):
        self.lst = []
        self.maxi = 0


    def book(self, startTime: int, endTime: int) -> int:
        self.lst.append((startTime, 1))
        self.lst.append((endTime, -1))
        self.lst.sort()

        res = 0
        for l in self.lst:
            res += l[1]
            self.maxi = max(self.maxi, res)
        
        return self.maxi



# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)