class MyQueue:
    def __init__(self):
        self.stack1 = []  # used for enqueue
        self.stack2 = []  # used for dequeue

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if not self.stack2:
            pass
