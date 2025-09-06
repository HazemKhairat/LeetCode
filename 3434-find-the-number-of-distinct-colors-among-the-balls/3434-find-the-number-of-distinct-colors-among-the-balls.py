class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        st = set()
        cnt = Counter()
        color = Counter()
        ans = [0] * len(queries)
        idx = 0
        for b, c in queries:
            if b in cnt:
                color[cnt[b]] -= 1
                if not color[cnt[b]]: st.remove(cnt[b])
                
            cnt[b] = c
            color[c] += 1
            st.add(c)
            ans[idx] = len(st)
            idx += 1
        return ans