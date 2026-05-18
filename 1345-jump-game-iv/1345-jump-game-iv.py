from collections import defaultdict


class Solution:
    def minJumps(self, arr: List[int]) -> int:

        dic = defaultdict(deque)
        n = len(arr)
        for i in range(n):
            dic[arr[i]].append(i)

        vis = set()
        q = deque()
        q.append((0, 0))  # index, step
        vis.add(0)

        while q:
            idx, step = q.popleft()
            # print("idx: ", idx)
            # print("number: ", arr[idx])
            if idx == n - 1:
                return step

            while dic[arr[idx]]:
                i = dic[arr[idx]].popleft()
                q.append((i, step + 1))
                vis.add(i)

            if (idx + 1) < n and idx + 1 not in vis:
                q.append((idx + 1, step + 1))
                vis.add(idx + 1)
            if (idx - 1) >= 0 and idx - 1 not in vis:
                q.append((idx - 1, step + 1))
                vis.add(idx - 1)

        return n
