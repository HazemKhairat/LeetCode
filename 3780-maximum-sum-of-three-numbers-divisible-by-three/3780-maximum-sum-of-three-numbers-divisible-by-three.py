from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = defaultdict(list)

        for num in nums:
            dic[num % 3].append(num)

        for i in range(3):
            dic[i].sort()

        p1 = dic[0][-1] + dic[1][-1] + dic[2][-1] if (len(dic[0]) and len(dic[1]) and len(dic[2])) else 0 # 0 1 2
        p2 = dic[0][-1] + dic[0][-2] + dic[0][-3] if len(dic[0]) >= 3 else 0 # 0 0 0
        p3 = dic[1][-1] + dic[1][-2] + dic[1][-3] if len(dic[1]) >= 3 else 0 # 1 1 1
        p4 = dic[2][-1] + dic[2][-2] + dic[2][-3] if len(dic[2]) >= 3 else 0  # 2 2 2
        
        

        return max([p1, p2, p3, p4])