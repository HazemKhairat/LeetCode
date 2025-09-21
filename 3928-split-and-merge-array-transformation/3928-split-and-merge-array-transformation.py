class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:

        if nums1 == nums2:
            return 0

        n = len(nums1)
        q = deque()
        vis = set()
        q.append((nums1, 0))  # curr_array , steps
        vis.add(tuple(nums1))

        while q:
            arr, steps = q.popleft()

            for l in range(n):
                for r in range(l, n):
                    sub = arr[l : r + 1]
                    tmp = arr[:l] + arr[r + 1 :]

                    for i in range(len(tmp)):
                        new_arr = tmp[:i] + sub + tmp[i:]
                        if new_arr == nums2:
                            return steps + 1

                        if tuple(new_arr) not in vis:
                            vis.add(tuple(new_arr))
                            q.append((new_arr, steps + 1))

        return 0
