class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)
        
        st = [set() for _ in range(m + 1)]

        for i in range(m):
            st[i + 1] = set(languages[i])
        
        bad_users = set()

        for u, v in friendships:
            if st[u].isdisjoint(st[v]):
                bad_users.add(u)
                bad_users.add(v)
            
        if not bad_users: return 0
        
        ans = 510
        for lang in range(1, n + 1):
            cnt = 0
            for user in bad_users:
                if lang not in st[user]:
                    cnt += 1
            
            ans = min(ans, cnt)

        return ans


        
            
