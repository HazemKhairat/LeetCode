class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        q = deque()

        q.append(0)
        far = 0

        while q:
            i = q.popleft()
            if i == n - 1:
                return True

            l = i + minJump
            r = min(i + maxJump, n - 1)

            for j in range(max(l, far), r + 1):
                if s[j] == "0":
                    q.append(j)

            far = r + 1

            # print(q)

        return False
