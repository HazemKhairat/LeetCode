class Solution:
    def maxAverageRatio(self, classes: List[List[int]], exS: int) -> float:
        pq = []
        for p, t in classes:
            ratio = p / t
            new_ratio = (p + 1) / (t + 1)
            possible_gain = new_ratio - ratio
            heapq.heappush(pq, [-possible_gain, p, t])

        

        while exS:
            gain, p, t = heapq.heappop(pq)
            p += 1 # 3
            t += 1 # 4
            new_gain = ((p + 1) / (t + 1)) - (p / t) # (4 / 5 ) - (3 / 4)
            heapq.heappush(pq, [-new_gain, p, t])
            exS -= 1

        ans = 0
        while pq:
            _, p, t = heapq.heappop(pq)
            ans += p / t
        return ans / len(classes)