class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        # if len(nums) % k == 0
        # and freq of each element <= k

        freq = Counter(nums)
        G = len(nums) // k
        for val in freq.values():
            if val > G:
                return False

        return len(nums) % k == 0