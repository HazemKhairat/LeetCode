class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = ans = 0
        n, m = len(nums1), len(nums2)

        while i < n and j < m:

            while i > j:
                j += 1

            if j == m or i == n:
                break

            if nums2[j] >= nums1[i]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1

        return ans
