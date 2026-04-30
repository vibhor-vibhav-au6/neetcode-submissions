class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        
        stack = []
        
        s_len = len(s)
        if not s_len: return True
        
        l = 0
        r = s_len - 1

        while l < r:
            if s[l] != s[r]: return False
            l += 1
            r -= 1
        
        return True

            
        