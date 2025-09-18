class FoodRatings:

    def __init__(self, f: List[str], c: List[str], r: List[int]):
        self.cnt = Counter()
        self.dic = defaultdict(list)
        for i in range(len(f)):
            self.cnt[f[i]] = [r[i], c[i]]
            heapq.heappush(self.dic[c[i]], [-r[i], f[i]])

    def changeRating(self, food: str, newRating: int) -> None:
        pq = self.dic[self.cnt[food][1]]
        self.cnt[food][0] = newRating
        heapq.heappush(pq, [-newRating, food])

    def highestRated(self, c: str) -> str:
        pq = self.dic[c]
        cnt = self.cnt
        while pq:
            r, f = pq[0]
            if -r == cnt[f][0]:
                return f
            heapq.heappop(pq)

        return ""


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
