class SegmentTree:
    def __init__(self, size):
        self.SIZE = size
        self.tree = [0] * (self.SIZE * 2)

    def update(self, idx, val):
        idx += self.SIZE
        self.tree[idx] = val
        while idx > 1:
            idx //= 2
            newVal = max(self.tree[2 * idx], self.tree[2 * idx + 1])
            if self.tree[idx] != newVal:
                self.tree[idx] = newVal
            else:
                return

    def query(self, l, r):
        max_space = 0
        left = l + self.SIZE
        right = r + self.SIZE

        while left <= right:
            if left % 2 == 1:
                max_space = max(max_space, self.tree[left])
                left += 1
            if right % 2 == 0:
                max_space = max(max_space, self.tree[right])
                right -= 1
            left //= 2
            right //= 2
        return max_space


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        max_boundary = 50005

        seg_tree = SegmentTree(max_boundary)
        seg_tree.update(max_boundary - 1, max_boundary - 1)

        obstacles = SortedList([0, max_boundary - 1])
        ans = []

        for q in queries:
            if q[0] == 1:
                x = q[1]
                next_idx = obstacles.bisect_right(x)
                nxt = obstacles[next_idx]
                prev = obstacles[next_idx - 1]

                seg_tree.update(x, x - prev)
                seg_tree.update(nxt, nxt - x)
                obstacles.add(x)
            else:
                x, sz = q[1], q[2]

                next_idx = obstacles.bisect_right(x)
                prev = obstacles[next_idx - 1]

                max_in_tree = seg_tree.query(0, prev)
                last_chunk = x - prev

                best_space = max(max_in_tree, last_chunk)
                ans.append(best_space >= sz)

        return ans
