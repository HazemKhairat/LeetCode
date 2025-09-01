class Solution:
    def maxAverageRatio(self, classes: List[List[int]], eS: int) -> float:
        
        pq = []
        for p, t in classes:
            gain = (p + 1) / (t + 1) - (p / t)
            heapq.heappush(pq, [-gain, p, t])
        
        while eS:
            gain, p, t = heapq.heappop(pq)
            p += 1
            t += 1
            gain = (p + 1) / (t + 1) - (p / t)
            heapq.heappush(pq, [-gain, p, t])
            eS -= 1

        ans = 0
        while pq:
            gain,p,t = heapq.heappop(pq)
            ans += p/t

        return ans / len(classes)