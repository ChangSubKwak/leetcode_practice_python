class MyQueue:

    def __init__(self):
        self.firstStack = []
        self.secondStack = []

    def push(self, x: int) -> None:
        self.firstStack.append(x)

    def pop(self) -> int:
        length = len(self.firstStack)
        for _ in range(length):
            self.secondStack.append(self.firstStack.pop())

        result = self.secondStack.pop()

        length = len(self.secondStack)
        for _ in range(length):
            self.firstStack.append(self.secondStack.pop())

        return result

    def peek(self) -> int:
        length = len(self.firstStack)
        for _ in range(length):
            self.secondStack.append(self.firstStack.pop())

        result = self.secondStack[-1]

        length = len(self.secondStack)
        for _ in range(length):
            self.firstStack.append(self.secondStack.pop())

        return result

    def empty(self) -> bool:
        return len(self.firstStack) == 0
