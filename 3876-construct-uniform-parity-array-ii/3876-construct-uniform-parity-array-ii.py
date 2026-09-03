class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        nums1.sort()
        # actually we only need the parity of the number not the value itself.
        for i in range(n):
            nums1[i] %= 2

        pref = [False] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] or (nums1[i - 1] == 1)

        print(pref)

        def construct(p):  # 0 -> even , 1 -> odd
            for i in range(n):
                # if nums1[i] not similar to the parity
                # and we can't change the parity using odd element in a prev index
                # then it's impossible to construct nums2
                if nums1[i] % 2 != p and not pref[i]:
                    return False

            return True

        return construct(0) or construct(1)
