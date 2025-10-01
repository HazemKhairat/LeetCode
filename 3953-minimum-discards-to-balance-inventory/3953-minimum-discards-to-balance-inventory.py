class Solution:
    def minArrivalsToDiscard(self, arr: List[int], w: int, m: int) -> int:
        cnt = Counter()
        q = deque()
        ans = 0

        for i in range(len(arr)):
            if q and q[0] <= i - w:
                cnt[arr[q.popleft()]] -= 1

            if cnt[arr[i]] < m:
                cnt[arr[i]] += 1
                q.append(i)
            else:
                ans += 1

        return ans
