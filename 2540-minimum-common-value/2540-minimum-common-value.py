class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        """two pointers"""

        # i, j = 0, 0
        # n, m = len(nums1), len(nums2)
        # while i < n and j < m:
        #     if nums1[i] == nums2[j]:
        #         return nums1[i]

        #     if nums1[i] < nums2[j]:
        #         i += 1
        #     else:
        #         j += 1

        # return -1

        """ Binary Search """

        def binary_search(target):

            left, right = 0, len(nums2) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums2[mid] == target:
                    return True
                elif nums2[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return False

        for num in nums1:
            if binary_search(num):
                return num

        return -1
