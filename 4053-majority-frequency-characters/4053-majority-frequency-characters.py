class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        cnt1 = Counter(s)
        cnt2 = defaultdict(set)

        for ch, freq in cnt1.items():
            cnt2[freq].add(ch)

        # print(cnt2)
        l = -1
        k = -1

        for key, arr in cnt2.items():
            if len(arr) > l or (len(arr) == l and key > k):
                l = len(arr)
                k = key

        return "".join(cnt2[k])
