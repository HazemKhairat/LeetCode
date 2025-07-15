class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowel = ['a', 'e', 'i', 'o','u']
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        lower = [chr(i) for i in range(97, 123)]
        upper = [chr(i) for i in range(65, 91)]

        f = s = l = False
        t = True
        for ch in word:
            if ch.lower() in vowel:
                f = True
            elif ch in lower or ch in upper or ch in digits:
                if ch.lower() not in vowel and ch not in digits:
                    l = True
                s = True
            else:
                t = False
        
        return f and s and t and l
            
            

      