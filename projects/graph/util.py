
# Note: This Queue class is sub-optimal. Why?
# It is sub-optimal because its using an array instead of a LinkedList.
# O(n) runtime to pop b/c we need to shift everything else over if we remove from front of queue. A real queue should be O(1)
# Doesnt affect Stack class b/c removing from the back in this instance.


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)
