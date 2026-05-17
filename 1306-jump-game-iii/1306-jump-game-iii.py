class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        vis = set()
        q = deque()
        q.append(start)  # index

        while q:
            idx = q.popleft()
            if arr[idx] == 0:
                return True
            vis.add(idx)

            right, left = idx + arr[idx], idx - arr[idx]
            if right < n and right not in vis:
                q.append(idx + arr[idx])
            if left >= 0 and left not in vis:
                q.append(idx - arr[idx])

        return False
