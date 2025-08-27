class TaskManager:
    # map task id to it's user
    # add [priority, taskId] to pq
    # add taskId -> priority to map
    # when excute if taskId in map pop and return userid
    # else pop 
    def __init__(self, tasks: List[List[int]]):
        self.task_user = defaultdict()
        self.task_prio = defaultdict()
        self.pq = []
        for u, t, p in tasks:
            self.task_user[t] = u
            self.task_prio[t] = p
            heapq.heappush(self.pq, (-p, -t))
        

    def add(self, u: int, t: int, p: int) -> None:
        pq = self.pq
        self.task_user[t] = u
        self.task_prio[t] = p
        heapq.heappush(pq, (-p, -t))

    def edit(self, t: int, p: int) -> None:
        self.task_prio[t] = p
        pq = self.pq
        heapq.heappush(pq, (-p, -t))

    def rmv(self, t: int) -> None:
        del self.task_user[t]
        del self.task_prio[t]

    def execTop(self) -> int:
        pq = self.pq
        # print("pq is " ,pq)
        # print("task_user : ", self.task_user)
        # print("task_priority: ", self.task_prio)
        
        while pq :
            p, t = heapq.heappop(pq) 
            taskId = -t
            priority = -p
            if taskId in self.task_prio and self.task_prio[taskId] == priority:
                user = self.task_user[taskId]
                del self.task_prio[taskId]
                del self.task_user[taskId]
                return user
        return -1
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()