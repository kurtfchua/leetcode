class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []

        for c in s: 
            if c in hashmap:
                stack.append(hashmap[c])
            elif stack and stack[-1] == c:
                stack.pop()
            else:
                return False
        
        return not stack

        # T O(n)
        # S O(n)
        