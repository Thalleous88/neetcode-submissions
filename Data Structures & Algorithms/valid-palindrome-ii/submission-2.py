class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i <= j:
    
            if s[i] != s[j]:
                skipL = s[i + 1 : j + 1]
                skipR = s[i : j]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            
            i += 1
            j -= 1

        return True

        
