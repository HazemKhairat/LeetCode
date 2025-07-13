class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        res = 0
        pq1, pq2 = [], []
        
        for player in players:
            heapq.heappush(pq1, player)
        
        for trainer in trainers:
            heapq.heappush(pq2, trainer)
        
        while pq1 and pq2:
            min1, min2 = heapq.heappop(pq1), heapq.heappop(pq2)
            if min1 <= min2:
                res += 1
            else:
                heapq.heappush(pq1, min1)

        return res