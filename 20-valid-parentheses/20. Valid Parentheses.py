class Solution:
    def isValid(self, s: str) -> bool:
        # iterate through string, if char is an open parenthesis add to stack 
        # if char is a close parenthesis check if its mapped open parenthesis pair is on top of the stack
        # if the paired open parenthesis is on top of the stack, pop and continue process
        # if stack is empty paranthesis is valid
        if len(s) < 2 or len(s)%2 != 0:
            return False

        par_dict = {
            ')': '(', 
            '}':'{',
            ']':'['
        }
        par_stack = []

        for char in s:
            if char in par_dict:
                if par_stack and (par_stack[-1] == par_dict[char]):
                    par_stack.pop()
                else:
                    return False
            else:
                par_stack.append(char)

        return not par_stack

    # Time Complexity O(n)
    # Space Complexity O(n)

        