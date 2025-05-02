class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter()

        for num in nums:
            cnt[num] += 1

        arr = []

        for num, freq in cnt.items():
            arr.append([freq, num])

        arr = sorted(arr, key=lambda x: (x[0], -x[1]))
        res = []
        for freq, num in arr:
            for i in range(freq):
                res.append(num)

        return res
