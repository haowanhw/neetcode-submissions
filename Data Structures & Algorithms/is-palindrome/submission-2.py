class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''

        for c in s:
            if c.isalpha() or c.isdigit():
            # Note isdigit() and isalnum() can only be applied to str
                newStr += c.lower()
        
        return newStr == newStr[::-1] # reverse the string
        
        