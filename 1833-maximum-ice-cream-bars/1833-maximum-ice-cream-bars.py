class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        m = max(costs)
        arr = [0] * (m + 1)

        for cost in costs:
            arr[cost] += 1

        ans = 0
        for i in range(1, m + 1):
            while coins - i >= 0 and arr[i] > 0:
                coins -= i
                ans += 1
                arr[i] -= 1

        return ans
