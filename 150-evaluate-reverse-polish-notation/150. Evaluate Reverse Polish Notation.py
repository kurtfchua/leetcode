class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token in ops:
                a, b = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(int(a) + int(b))

                elif token == "-":
                    stack.append(int(b) - int(a))

                elif token == "*":
                    stack.append(int(a) * int(b))

                else:
                    stack.append(int(int(b) / int(a)))
            else:
                stack.append(int(token))
        
        return stack[-1]