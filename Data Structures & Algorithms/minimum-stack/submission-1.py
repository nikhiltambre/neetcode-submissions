class MinStack:
    def __init__(self):
        self.stack = deque()
        self.minvals = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        currentMIN = min(self.minvals[-1], val) if self.minvals else val
        self.minvals.append(currentMIN)

    def pop(self) -> None:
        self.stack.pop()
        self.minvals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minvals[-1]
