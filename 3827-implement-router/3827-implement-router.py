class Router:
    
    def __init__(self, ml: int):
        self.rt = deque()
        self.st = SortedSet() 
        self.dic = defaultdict(deque)
        self.ml = ml

    def addPacket(self, s: int, d: int, t: int) -> bool:
        rt, st, dic, ml = self.rt, self.st, self.dic, self.ml
        packet = (s, d, t)
        if packet in st:
            return False

        if len(rt) == ml:
            tmp = rt.popleft()
            st.remove(tmp)
            dic[tmp[1]].popleft()
        
        rt.append(packet)
        st.add(packet)
        dic[d].append(packet[2])

        return True

    def forwardPacket(self) -> List[int]:
        rt = self.rt
        st = self.st
        dic = self.dic
        if rt:
            s, d, t = rt.popleft()
            st.remove((s, d, t))
            dic[d].popleft()
            return [s, d, t]
        return []
        

    def getCount(self, d: int, s: int, e: int) -> int:
        l = bisect_left(self.dic[d], s)
        r = bisect_right(self.dic[d], e)
        return r - l

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)