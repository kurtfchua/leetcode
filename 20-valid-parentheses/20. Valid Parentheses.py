class Solution:
    def isValid(self, s: str) -> bool:
        # use stack to keep track of the updated 
        # closing parenthesis when new opening parentheisis is found
        # when we encounter a closing parenthesis, 
        # we check if it is equal to the elem on top of stack
        # otherwise we return False
        # we use a dictionary to keep track of the pairs
        # if stack size is 0 all parenthesis are closed properly ahd we return True
        # otherwise return False

        stack = []
        dict = {
                "(": ")",
                "[": "]",
                "{":"}"
                    }
        
        for char in s:
            if char in dict:
                stack.append(dict[char])
            else:
                if stack and stack[-1] == char:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0

        # Space Complexity: We create a stack in the worst case will copy all of the string, O(n)
        # Time Complexity: We need to go through the entire string to check if it is valid, O(n)

        