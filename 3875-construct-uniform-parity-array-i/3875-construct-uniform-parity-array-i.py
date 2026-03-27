class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:

        n = len(nums1)

        def find(i, parity):
            for j in range(n):
                if j == i:
                    continue
                if (nums1[i] - nums1[j]) % 2 == parity:
                    return True
            return False

        def solve(parity):
            for i in range(n):
                if (nums1[i] % 2 != parity) and (not find(i, parity)):
                    return False

            return True

        return solve(0) or solve(1)
