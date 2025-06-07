class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        st = set()
        smallest = -1
        pq = []
        flag = False
        i = 0
        while i < n:
            if s[i] != "*":
                heapq.heappush(pq, (s[i], -i))
            while i < n and s[i] == "*" and pq:
                item = heapq.heappop(pq)
                st.add(-1 * item[1])
                flag = True
                i += 1

            if flag:
                flag = False
                continue
            i += 1

        print(st)

        res = ""
        for i in range(n):
            if i in st or s[i] == "*":
                continue
            res += s[i]

        return res
