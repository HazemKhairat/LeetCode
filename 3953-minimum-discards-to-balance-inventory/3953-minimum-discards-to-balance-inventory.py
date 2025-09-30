class Solution:
    def minArrivalsToDiscard(self, a: List[int], w: int, m: int) -> int:
        q = deque()
        cnt = Counter()
        ans = 0
        for i in range(len(a)):
            while q and q[0] <= i - w:
                idx = q.popleft()
                cnt[a[idx]] -= 1

            if cnt[a[i]] < m:
                cnt[a[i]] += 1
                q.append(i)
            else:
                ans += 1

        return ans
