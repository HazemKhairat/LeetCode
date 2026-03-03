class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        s = "0"

        def invert(st):
            st = list(st)
            for i in range(len(st)):
                if st[i] == "0":
                    st[i] = "1"
                else:
                    st[i] = "0"
            return "".join(st)

        def reverse(st):
            st = list(st)
            return "".join(st[::-1])

        while n > 1:
            new_s = s + "1" + reverse(invert(s))
            s = new_s
            n -= 1

        return s[k - 1]
