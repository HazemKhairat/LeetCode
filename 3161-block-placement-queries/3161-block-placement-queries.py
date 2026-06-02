class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (self.size * 2)

    def update(self, idx, val):
        idx += self.size
        self.tree[idx] = val

        while idx > 1:
            idx //= 2
            newVal = max(self.tree[idx * 2 + 1], self.tree[idx * 2])
            if self.tree[idx] != newVal:
                self.tree[idx] = newVal
            else:
                return

    def query(self, l, r):
        left = l + self.size
        right = r + self.size
        maxi = -inf
        while left <= right:
            if right % 2 == 0:
                maxi = max(maxi, self.tree[right])
                right -= 1

            if left % 2 == 1:
                maxi = max(maxi, self.tree[left])
                left += 1

            left //= 2
            right //= 2

        return maxi


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        ans = []
        seg_tree = SegmentTree(50005)
        obstcals = SortedList([0, 50001])
        seg_tree.update(50000, 50000)

        for q in queries:
            op, x = q[0], q[1]

            if op == 1:
                nxt_idx = obstcals.bisect_right(x)
                nxt = obstcals[nxt_idx]
                prev = obstcals[nxt_idx - 1]
                seg_tree.update(nxt, nxt - x)
                seg_tree.update(x, x - prev)
                obstcals.add(x)
            else:
                nxt_idx = obstcals.bisect_right(x)
                prev = obstcals[nxt_idx - 1]
                max_space = max(seg_tree.query(0, prev), x - prev)
                ans.append(max_space >= q[2])

        return ans
