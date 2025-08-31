class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:

        st = set()
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                st.add(i)
                st.add(n // i)
        divs = sorted(st)

        mini = inf
        ans = []

        def solve(rem, idx, curr):
            nonlocal ans, mini
            if len(curr) == k - 1:
                last = rem
                if curr and last >= curr[-1]:
                    curr.append(last)
                    if mini > (curr[-1] - curr[0]):
                        mini = curr[-1] - curr[0]
                        ans = curr[:]
                    curr.pop()
                return

            for i in range(idx, len(divs)):
                if rem % divs[i] != 0:
                    continue
                if divs[i] > rem:
                    break

                curr.append(divs[i])
                solve(rem // divs[i], i, curr)
                curr.pop()

        solve(n, 0, [])

        return ans
