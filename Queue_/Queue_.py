
class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.data)

class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.length = 0

    def __repr__(self):
        """Returns linked list as string."""
        result = ''
        tmp = self.head
        while tmp:
            result += str(tmp.data) + ' -> '
            tmp = tmp.next
        result += 'None'
        return result

    def __len__(self):
        """Returns length of linked list."""
        return self.length

    def enqueue(self, data):
        """Adds new node on the left (head)."""
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def dequeue(self):
        """Removes and returns right-most node (tail)."""
        result = self.tail.data
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        if self.length > 0: self.length -= 1
        return result

#%%
Q = Queue()
Q
len(Q)
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.dequeue()







