class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        nums1 = [num % 2 for num in nums1]
        cnt = Counter(nums1)
        nums2 = [None] * n

        def construct(p):
            for i in range(n):
                if nums1[i] % 2 != p and cnt[1] - nums1[i] <= 0:
                    return False

            return True

        if construct(0) or construct(1):
            return True

        return False
