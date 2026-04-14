class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        # create a set to access elements in O(1)
        st = set(nums)

        # check the chain of each item
        for num in st:

            # start only if it is the begainng of the chain
            if (num - 1) not in st:
                curr = num
                count = 1
                while (curr + 1) in st:
                    curr += 1
                    count += 1

                ans = max(ans, count)

        return ans
