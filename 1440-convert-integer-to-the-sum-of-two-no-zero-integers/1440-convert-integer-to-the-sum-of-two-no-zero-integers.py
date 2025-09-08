class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a, b = 1, n - 1

        def valid(a, b):
            while a:
                if a % 10 == 0:
                    return False
                a //= 10
            while b:
                if b % 10 == 0:
                    return False
                b //= 10
            return True
        while True:
            if valid(a, b):
                return [a, b]
            a += 1
            b -= 1
        
        return [a, b]
