class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        m = n // 3
        part1 = [0] * (m + 1)
        pq = [-x for x in nums[:m]]
        heapq.heapify(pq)
        total = sum(nums[:m])
        part1[0] = total
        for i in range(m ,2 * m):
            total += nums[i]
            heapq.heappush(pq, -nums[i])
            total += heappop(pq)
            part1[i - m + 1] = total
        
        total2 = sum(nums[2*m:])
        pq2 = [x for x in nums[2 * m:]]
        heapq.heapify(pq2)
        res = part1[m] - total2

        for i in range(2 * m - 1, m - 1, -1):
            total2 += nums[i]
            heapq.heappush(pq2, nums[i])
            total2 -= heapq.heappop(pq2)
            res = min(res, part1[i - m] - total2)


        return res