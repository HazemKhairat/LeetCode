class Solution:
    def minArrivalsToDiscard(self, arr: List[int], w: int, m: int) -> int:
        n = len(arr)
        maxi = max(arr)
        keep = [False] * n
        cnt = [0] * (maxi + 1)
        ans = 0

        for i in range(n):
            j = i - w
            if j >= 0 and keep[j]:
                prev = arr[j]
                cnt[prev] -= 1
            
            curr = arr[i]
            if cnt[curr] < m:
                cnt[curr] += 1
                keep[i] = True
            else:
                ans += 1
                keep[i] = False

        return ans