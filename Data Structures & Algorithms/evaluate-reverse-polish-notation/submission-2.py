import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }
        for c in tokens:
            if c in ops:
                first = int(stack.pop())
                second = int(stack.pop())
                stack.append(ops[c](second,first))
            else:
                stack.append(c)
        return int(stack.pop())