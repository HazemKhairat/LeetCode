class Solution:
    def maxTotal(self, v: List[int], l: List[int]) -> int:
        li = []
        cnt = Counter()
        for i, j in zip(v, l):
            li.append((j, -i))
        li.sort()

        total = 0
        active = 0
        notActive = set()
        
        for item in li:
            if item[0] in notActive:
                continue

            x = -item[1]

            if active < item[0]:
                total += x
                cnt[item[0]] += 1
                active += 1
                
            if cnt[active]:
                notActive.add(active)
                num = cnt[active]
                cnt[active] = 0
                active -= num
        return total 
                
            
        

        
        