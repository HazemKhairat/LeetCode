class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Binary Search : upper_bound algorithm

        idx = bisect.bisect_right(letters, target)
        
        return letters[idx] if idx < len(letters) else letters[0]
