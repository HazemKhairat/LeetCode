from sortedcontainers import SortedList

class MedianFinder:
    arr = None
    def __init__(self):
        self.arr = SortedList()


    def addNum(self, num: int) -> None:
        self.arr.add(num)

    def findMedian(self) -> float:
        n = len(self.arr)
        median = n // 2
        if n % 2 == 1:
            i = 0
            for item in self.arr:
                if i == median:
                    return item
                i += 1
        else:
            i = 0
            prev = 0
            curr = 0
            for item in self.arr:
                if i == median - 1:
                    prev = item
                if i == median:
                    curr = item
                    break
                i += 1
            return float(prev + curr) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()