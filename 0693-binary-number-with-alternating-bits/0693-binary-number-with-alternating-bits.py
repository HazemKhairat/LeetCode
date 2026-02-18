class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        prev = n % 2
        n //= 2
        while n:
            curr = n % 2
            print(prev)
            print(curr)
            if prev == curr:
                return False
            prev = curr
            n //= 2
        return True
