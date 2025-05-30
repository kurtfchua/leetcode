class Solution:
    def isValid(self, s: str) -> bool:
        hm = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for c in s: 
            if c in hm: 
                stack.append(hm[c])
            elif stack and stack[-1] == c:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0


        