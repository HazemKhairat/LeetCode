class Solution:
    def generateTag(self, caption: str) -> str:
        arr = caption.split()
        if not arr:
            return '#'
        res = "#"
        res += arr[0].lower()
        
            
        for i in range(1, len(arr)):
            word = arr[i]
            res += word[0].upper()
            res += word[1:].lower()
            
        return res[:100] if len(res) > 100 else res