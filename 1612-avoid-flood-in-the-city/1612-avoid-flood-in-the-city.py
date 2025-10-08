class Solution:
    def avoidFlood(self, r: List[int]) -> List[int]:
        n = len(r)
        ans = [1] * n
        cnt = Counter()  # last index of lake rains
        st = SortedSet()  # Sorted Sunny Days

        for i, num in enumerate(r):
            if num == 0:
                st.add(i)
            else:
                ans[i] = -1

                if num in cnt:
                    last_idx = cnt[num]
                    idx = st.bisect_left(last_idx)
                    if idx == len(st):
                        return []
                    ans[st[idx]] = num
                    st.discard(st[idx])

                cnt[num] = i

        return ans
