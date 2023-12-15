# Implement Stack using Queue

from collections import deque


class MyStack:
    def __init__(self):
        self.queue1 = deque()

    def push(self, x):
        self.queue1.append(x)
        # Reorder the elements so that the recently pushed element is at the front
        for _ in range(len(self.queue1) - 1):
            self.queue1.append(self.queue1.popleft())

    def pop(self):
        return self.queue1.popleft()

    def top(self):
        return self.queue1[0]

    def empty(self):
        return not bool(self.queue1)


stack = MyStack()
stack.push(1)
stack.push(2)

print("Top: ", stack.top())
print("Pop: ", stack.pop())
print("Empty: ", stack.empty())
