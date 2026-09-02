class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        nums2 = [None] * n

        def construct(p):
            for i in range(n):
                if nums1[i] % 2 == p:
                    nums2[i] = nums1[i]
                else:
                    for j in range(n):
                        if i == j:
                            continue
                        if (nums1[i] - nums1[j]) % 2 == p:
                            nums2[i] = nums1[i] - nums1[j]

            return not (any(nums2) == 0)

        if construct(0) or construct(1):
            return True

        return False
