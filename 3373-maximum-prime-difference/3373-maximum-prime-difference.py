class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:

        limit = max(nums) + 1
        primes = [True] * limit
        def sieve():
            
            primes[0] = primes[1] = False
            for i in range(2, int(sqrt(limit)) + 1):
                if primes[i]:
                    for j in range(i*i, limit, i):
                        primes[j] = False
                        
            return primes

        sieve()

        f = 0
        for i in range(len(nums)):
            if primes[nums[i]]:
                f = i
                break

        s = 0
        for i in range(len(nums) - 1, -1, -1):
            if primes[nums[i]]:
                s = i
                break
                
        return s - f