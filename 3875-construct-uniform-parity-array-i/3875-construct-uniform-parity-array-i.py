class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        nums2 = [None] * n

        # even elements construction
        for i in range(n):
            if nums1[i] % 2 == 0:
                nums2[i] = nums1[i]
            else:
                for j in range(n):
                    if i == j:
                        continue
                    if (nums1[i] - nums1[j]) % 2 == 0:
                        nums2[i] = nums1[i] - nums1[j]

        if not any(nums2) == None:
            return True

        # odd elements construction
        for i in range(n):
            if nums1[i] % 2 == 1:
                nums2[i] = nums1[i]
            else:
                for j in range(n):
                    if i == j:
                        continue
                    if (nums1[i] - nums1[j]) % 2 == 1:
                        nums2[i] = nums1[i] - nums1[j]

        if not any(num2) == None:
            return True

        return False
