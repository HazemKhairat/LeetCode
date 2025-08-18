class Solution:
    def processQueries(
        self, c: int, co: List[List[int]], q: List[List[int]]
    ) -> List[int]:
        online = set([x for x in range(1, c + 1)])
        ans = []

        parents = [0] * (c + 1)
        for i in range(1, c + 1):
            parents[i] = i

        def find(n):
            if n == parents[n]:
                return n
            parents[n] = find(parents[n])
            return parents[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return
            parents[p1] = p2

        

        for u, v in co:
            union(u, v)

        pq_dict = defaultdict(list)
        for node in range(1, c + 1):
            parent = find(node)
            heapq.heappush(pq_dict[parent], node)

        for num, x in q:
            if num == 1:
                if x in online:
                    ans.append(x)
                else:
                    parent = find(x)
                    tmp_pq = pq_dict[parent]
                    while tmp_pq and tmp_pq[0] not in online:
                        heapq.heappop(tmp_pq)
                    ans.append(tmp_pq[0] if tmp_pq else -1)
            elif x in online:
                online.remove(x)

        return ans
