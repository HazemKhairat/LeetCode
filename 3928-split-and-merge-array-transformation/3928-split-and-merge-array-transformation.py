class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1 == nums2: return 0
        q = deque()
        q.append((nums1, 0))  # arr, operation_num
        vis = set(tuple(nums1))
        n = len(nums1)
        while q:
            arr, op = q.popleft()
            for l in range(n):
                for r in range(l, n):
                    rmv = arr[l : r + 1]
                    tmp = arr[:l] + arr[r + 1 :]
                    for k in range(len(tmp)):
                        new_arr = tmp[:k] + rmv + tmp[k:]
                        if new_arr == nums2:
                            return op + 1
                        if tuple(new_arr) not in vis:
                            vis.add(tuple(new_arr))
                            q.append((new_arr, op + 1))
        return 0
