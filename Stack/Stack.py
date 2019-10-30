class Stack:
    """Stack implementation using list built in type."""
    def __init__(self):
        self.items = []

    def __repr__(self):
        return repr(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print('Stack is empty.')
            return
        return self.items[-1]

    def size(self):
        return len(self.items)

#%%
S1 = Stack()
S1.is_empty()
S1.push(1)
S1.push(2)
S1.push(3)
S1.push(4)
print(S1)
while not S1.is_empty():
    print(S1.pop())
print(S1)
