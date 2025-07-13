class SummaryRanges:

    def __init__(self):
        self.arr = []
        self.st = set()

    def addNum(self, value: int) -> None:
        if value in self.st:
            return
        self.arr.append(value)
        self.st.add(value)

    def getIntervals(self) -> List[List[int]]:
        nums = self.arr
        nums.sort()
        i = 0
        j = 1
        res = []
        while i < len(nums):
            while j < len(nums) and nums[j] - nums[j - 1] == 1:
                j += 1
            interval = [nums[i], nums[j - 1]]
            i = j
            j += 1
            res.append(interval)

        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
