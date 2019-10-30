
class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedStack:

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        if self.head == None:
            return True
        return False

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def pop(self):
        if self.is_empty():
            return None
        popped = self.head.data
        self.head = self.head.next
        self.size -= 1
        return popped

#%%
S = LinkedStack()
len(S)
S.is_empty()
S.push('hi')
S.pop()
S.peek()

