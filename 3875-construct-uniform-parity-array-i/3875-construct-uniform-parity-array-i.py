class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        for i in range(n): nums1[i] %= 2
        
        cnt = Counter(nums1)  # Space O(1), only 2 values stored: 1 or 0

        def construct(p):  # 0 -> even , 1 -> odd
            for i in range(n):
                if nums1[i] % 2 != p and cnt[1] - nums1[i] <= 0:
                    return False

            return True

        return construct(0) or construct(1)
