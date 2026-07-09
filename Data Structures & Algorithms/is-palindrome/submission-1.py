class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''

        for c in s:
            if ('A' <= c <= 'Z') or ('a' <= c <= 'z') or ('0' <= c <= '9'):
            # Note that '0' and '9' are character, not digit here
                newStr += c.lower()
        
        return newStr == newStr[::-1] # reverse the string
        
        