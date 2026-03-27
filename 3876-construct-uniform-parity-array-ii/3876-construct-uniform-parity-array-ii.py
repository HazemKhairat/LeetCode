class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:

        n = len(nums1)
        odd = [num for num in nums1 if num % 2 == 1]
        odd.sort()

        def find(i, parity):
            pos = bisect.bisect_left(odd, nums1[i])
            if pos == len(odd):
                return True
            return (pos != 0) and (nums1[i] != odd[pos])

        def solve(parity):
            for i in range(n):
                if (nums1[i] % 2 != parity) and (not find(i, parity)):
                    return False

            return True

        return solve(0) or solve(1)
