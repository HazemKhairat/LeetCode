class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return sum(cost)

        cost.sort(key=lambda x: -x)
        # print(cost)
        ans = 0

        i = 2
        while i < len(cost):
            ans += cost[i - 1] + cost[i - 2]
            i += 3

        if len(cost) % 3 != 0:
            i -= 2
            ans += sum(cost[i:])

        return ans
