class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        arr = [[float('inf')] * 3 for _ in range(n)]
        # print(arr)

        for i in range(n):
            arr[i][1] = (ratings[i], i)
            if i > 0:
                arr[i][0] = (ratings[i - 1], i - 1)
            if i < n - 1:
                arr[i][2] = (ratings[i + 1], i + 1)
        arr = sorted(arr, key=lambda x: x[1])

        candies = Counter()
        for i in range(n):
            item = arr[i][1]
            candies[item] = 1
        print(arr)

        for i in range(1, n):
            curr, last, next = arr[i][1], arr[i][0], arr[i][2]
            if  last != float('inf') and curr[0] > last[0] and candies[curr] <= candies[last]:
                candies[curr] = candies[last] + 1
            if next != float('inf') and curr[0] > next[0] and candies[curr] <= candies[next]:
                candies[curr] = candies[next] + 1

        res = 0 
        for [c, num] in candies.items():
            res += num
        return res