class Solution:
    def isValid(self, s: str) -> bool:
        paren = {'(':')', '{':'}', '[':']'}
        stack = []

        for c in s:
            if c in paren: 
                stack.append(paren[c])
            elif stack and stack[-1] == c:
                stack.pop()
            else:
                return False
        
        return not stack        