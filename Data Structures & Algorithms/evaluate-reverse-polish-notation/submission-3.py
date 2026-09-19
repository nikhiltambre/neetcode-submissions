import operator


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for c in tokens:
            if c == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif c == "-":
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(b - a)
            elif c == "*":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a * b)
            elif c == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b) / int(a)))
            else:
                stack.append(c)

        return int(stack.pop())
