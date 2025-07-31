class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)

        def sieve(n):
            if n < 2:
                return set()
            primes = [True] * n
            primes[0] = primes[1] = False

            for i in range(2, int(n**0.5) + 1):
                if primes[i]:
                    for j in range(i*i, n, i):
                        primes[j] = False

            return set([i for i, is_prime in enumerate(primes) if is_prime])

        primes = sieve(n)
        A, B = 0, 0
        for i, num in enumerate(nums):
            if i in primes:
                A += num
            else:
                B += num

        return abs(A - B)
            