class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []

        for c in s: 
            if c in mp:
                stack.append(mp[c])
            elif stack and stack[-1] == c:
                stack.pop()
            else:
                return False
        
        return not stack
        