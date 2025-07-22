class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        cnt = Counter(nums)

        def isPrime(num):
            if num < 2:
                return False
            if num == 2:
                return True
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
            
        for key, value in cnt.items():
            if isPrime(value):
                return True

        return False