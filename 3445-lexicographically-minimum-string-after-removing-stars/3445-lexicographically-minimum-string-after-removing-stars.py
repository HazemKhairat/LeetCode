class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        st = set()
        pq = []
        i = 0
        while i < n:
            if s[i] != "*":
                heapq.heappush(pq, (s[i], -i))
                i += 1

            while i < n and s[i] == "*" and pq:
                item = heapq.heappop(pq)
                st.add(-1 * item[1])
                i += 1

        res = ""
        for i in range(n):
            if i in st or s[i] == "*":
                continue
            res += s[i]

        return res
