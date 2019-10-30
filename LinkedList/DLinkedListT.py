
class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.data)

class DLinkedListT:
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

    def add_first(self, data):
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

    def add_last(self, data):
        """Adds new node on the right (tail)."""
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop_first(self):
        """Removes and returns left-most node (head)."""
        result = self.head
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        if self.length > 0: self.length -= 1
        return result

    def pop_last(self):
        """Removes and returns right-most node (tail)."""
        result = self.tail
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        if self.length > 0: self.length -= 1
        return result

#%%
DLL = DLinkedListT()
DLL.add_first(1)
DLL.add_first(2)
DLL.add_first(3)
DLL.add_first(4)
DLL.add_first(5)
DLL.add_first(6)
DLL.add_last(12)

DLL.pop_first()
DLL.pop_last()

DLL.head
DLL.tail

len(DLL)

print(DLL)





















































