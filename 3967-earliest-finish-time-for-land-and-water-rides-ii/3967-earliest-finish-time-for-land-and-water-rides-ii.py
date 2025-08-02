class Solution:
    def earliestFinishTime(self, ls: List[int], ld: List[int], ws: List[int], wd: List[int]) -> int:
        
        lands = [start + dur for start, dur in zip(ls, ld)]
        
        waters = [start + dur for start, dur in zip(ws, wd)]
        
        minLand = min(lands)
        option1 = min( max(minLand, ws[j]) + wd[j] for j in range(len(ws)))
        
        minWater = min(waters)
        option2 = min( max(minWater, ls[i]) + ld[i] for i in range(len(ls)))
        
        return min(option1, option2)