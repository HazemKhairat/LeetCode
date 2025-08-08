class Router:

    def __init__(self, ml: int):
        self.ml = ml
        self.li = deque()
        self.s = set()
        self.h = defaultdict(deque)

    def addPacket(self, s: int, d: int, t: int) -> bool:
        packet = (s, d, t)
        if packet in self.s:
            return False

        if len(self.li) == self.ml:
            tmp = self.li.popleft()
            self.s.remove(tmp)
            self.h[tmp[1]].popleft()

        self.s.add(packet)
        self.li.append(packet)
        self.h[d].append(t) 
        return True

    def forwardPacket(self) -> List[int]:
        arr = []
        if self.li:
            arr = self.li.popleft()
            self.s.remove(arr)
            self.h[arr[1]].popleft()
        return list(arr)

    def getCount(self, d: int, st: int, e: int) -> int:
        li = self.h[d]
        # print(li)
        l, r = 0, len(li) - 1

        while l <= r:
            mid = (l + r) // 2
            if li[mid] >= st:
                r = mid - 1
            else:
                l = mid + 1
        leftMost = l
        # print(l)
        l, r = 0, len(li) - 1

        while l <= r:
            mid = (l + r) // 2
            if li[mid] <= e:
                l = mid + 1
            else:
                r = mid - 1
        rightMost = r

        print(r)
        return rightMost - leftMost + 1


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
