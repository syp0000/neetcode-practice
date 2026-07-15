class MinStack:

    def __init__(self):
        self.stack = []
        self.MinStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.MinStack:
            self.MinStack.append(val)
        elif val <= self.MinStack[-1]:
            self.MinStack.append(val)
        

    def pop(self) -> None:
        if self.stack[-1] == self.MinStack[-1]:
            self.MinStack.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.MinStack[-1]
        
