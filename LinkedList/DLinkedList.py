
class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.data)

class DLinkedList:
    def __init__(self, head=None):
        self.head = head

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
        counter = 0
        tmp = self.head
        while tmp:
            counter += 1
            tmp = tmp.next
        return counter

    def add_start(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def add_last(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            return
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = new_node

    def insert_at_pos(self, pos, new_data):
        """Inserts new data as a node at a given
        positional index."""
        if pos == 0:
            self.add_start(new_data)
        else:
            new_node = Node(new_data)
            tmp = self.head
            for i in range(1, pos):
                tmp = tmp.next
            new_node.next = tmp.next
            tmp.next = new_node
            new_node.prev = tmp
            new_node.next.prev = new_node

    def insert_at_ref(self, mid_node, new_data):
        """Inserts new data as a node after the node
        with known pointer."""
        if mid_node == None:
            raise ValueError("Middle node is None")
        else:
            new_node = Node(new_data)
            new_node.next = mid_node.next
            mid_node.next = new_node
            new_node.prev = mid_node
            new_node.next.prev = new_node

    def remove_at_pos(self, pos):
        """Removes a node at a given positional index."""
        if pos == 0:
            self.head = self.head.next

        else:
            tmp = self.head
            for i in range(1, pos):
                tmp = tmp.next
            tmp.next = tmp.next.next
            if tmp.next:
                tmp.next.prev = tmp

    def remove_at_ref(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        node.prev = None
        node.next = None

    def get_node_at_pos(self, pos):
        """Returns node at a given positional index."""
        tmp = self.head
        for i in range(0, pos):
            if tmp == None: print('None reached during iteration.')
            tmp = tmp.next
        return tmp

    def concatenate(self, second_list):
        """Concatenates two linked lists."""
        if not self.head and second_list.head:
            self.head = second_list.head
        elif self.head:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = second_list.head
            second_list.head.prev = tmp

    def split_after(self, pos):
        """Split current list after given positional index
        and return second list."""
        tmp = self.head
        for i in range(0, pos):
            tmp = tmp.next
        new_list = DLinkedList(tmp.next)
        tmp.next = None
        new_list.head.prev = None
        return new_list

    def reverse(self):
        """Reverse doubly linked list in place.
            Time complexity O(n)."""
        curr = self.head
        prev_node = None
        while curr:
            prev_node = curr.prev
            curr.prev = curr.next
            curr.next = prev_node
            curr = curr.prev
        self.head = prev_node.prev

#%%
DLL = DLinkedList()
DLL.add_start(1)
DLL.add_start(2)
DLL.add_start(3)
DLL.add_start(4)
DLL.add_start(5)
DLL.add_start(6)
print(DLL)





















































