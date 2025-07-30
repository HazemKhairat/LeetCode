class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        for i in range(len(cost) - 1):
            if cost[i] < cost[i + 1]:
                cost[i + 1] = cost[i]

        return cost
        