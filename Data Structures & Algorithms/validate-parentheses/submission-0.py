class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen: # if c in a closing parenthesis
                if stack and stack[-1] == closeToOpen[c]: 
                    stack.pop()
                else:
                    return False
            else: # if c is an opening parenthesis
                stack.append(c)
        
        return True if not stack else False
        