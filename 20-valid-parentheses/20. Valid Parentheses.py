class Solution:
    def isValid(self, s: str) -> bool:
        # iterate through the string, if close parenthesis pop stack if the correspoding open parenthesis is
        # on top of the stack, otherwise add open parenthesis to the stack
        # if stack has len 0, then all open parenthesis in the stack were closed return true, otherwise return false

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
         

