class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []

    def push(self, val: int) -> None:
        if not self.prefix or val <= self.prefix[-1]:
            self.prefix.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        elem = self.stack.pop()
        if elem == self.prefix[-1]:
            self.prefix.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix[-1]
        
'''
[1]

[]
'''