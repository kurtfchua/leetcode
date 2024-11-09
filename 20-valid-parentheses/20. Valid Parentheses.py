class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        hashmap = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for c in s:
            if c in hashmap:
                if stack and hashmap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack
         

