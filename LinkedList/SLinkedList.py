class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class SLinkedList:

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
        """Adds new node with given data at
        beginning and makes it the new head."""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, new_data):
        """Traverses linked list to find tail node
        then adds new data as a last node."""
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
        else:
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

    def insert_at_ref(self, mid_node, new_data):
        """Inserts new data as a node after the node
        with known pointer."""
        if mid_node == None:
            raise ValueError("Middle node is None")
        else:
            new_node = Node(new_data)
            new_node.next = mid_node.next
            mid_node.next = new_node

    def remove_at_pos(self, pos):
        """Removes a node at a given positional index."""
        if pos == 0:
            self.head = self.head.next
        else:
            tmp = self.head
            for i in range(1, pos):
                tmp = tmp.next
            tmp.next = tmp.next.next

    def get_node_at_pos(self, pos):
        """Returns node at a given positional index."""
        tmp = self.head
        for i in range(0, pos):
            if tmp == None: print('None reached during iteration.')
            tmp = tmp.next
        return tmp

    def concatenate(self, second_list):
        """Concatenates two linked lists. Joins head of second list
        with the tail of current list."""
        if self.head == None and second_list.head != None:
            self.head = second_list.head
        elif self.head != None:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = second_list.head

    def split_after(self, pos):
        """Split current list after given positional index
        and return second list."""
        tmp = self.head
        for i in range(0, pos):
            tmp = tmp.next
        new_list = SLinkedList(tmp.next)
        tmp.next = None
        return new_list

    def reverse(self):
        """Reverses linked list in place.
            Time complexity O(n)."""
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node

if __name__ == '__main__':
#%% Test "add_start"
    list1 = SLinkedList()
    list1.add_start(1)
    list1.add_start(2)
    list1.add_start(3)
    print(list1)

    list2 = SLinkedList()
    list2.add_start('Mon')
    list2.add_start('Tue')
    list2.add_start('Wed')

#%% Test "add_last"
    list1 = SLinkedList()
    print(list1)
    print('length:', len(list1))

    list1.add_start(1)
    list1.add_start(2)
    list1.add_start(3)
    print(list1)
    print('length:', len(list1))

    list1.add_last(9)
    print(list1)
    print('length:', len(list1))

#%% Test "insert_at_pos"
    list1 = SLinkedList()
    list1.add_start(1)
    list1.add_start(2)
    list1.add_start(3)
    list1.add_start(4)
    print(list1)
    list1.insert_at_pos(2, 999)
    print(list1)

#%% Test "insert_at_ref"
    list2 = SLinkedList()
    list2.add_start(1)
    list2.add_start(2)
    list2.add_start(3)
    list2.add_start(4)
    print(list2)
    some_node = list2.head.next.next
    print(some_node.data)
    list2.insert_at_ref(some_node, 999)
    print(list2)

#%% Test "remove_at_pos"
    list1 = SLinkedList()
    list1.add_start(1)
    list1.add_start(2)
    list1.add_start(3)
    list1.add_start(4)
    list1.add_start(5)
    print(list1)
    list1.remove_at_pos(2)
    print(list1)

#%% Test "concatenate"
    L1 = SLinkedList()
    L1.add_start(1)
    L1.add_start(2)
    L1.add_start(3)
    L2 = SLinkedList()
    L2.add_start(4)
    L2.add_start(5)
    L2.add_start(6)
    print(L1)
    print(L2)
    L1.concatenate(L2)
    print(L1)
    print(L2)

#%% Test "get_node_at_pos"
    L1 = SLinkedList()
    L1.add_start(1)
    L1.add_start(2)
    L1.add_start(3)
    L1.add_start(4)
    print(L1)
    N = L1.get_node_at_pos(0)
    print(N.data)

#%% Test "split_after"
    L1 = SLinkedList()
    L1.add_start(1)
    L1.add_start(2)
    L1.add_start(3)
    L1.add_start(4)
    print(L1)
    L2 = L1.split_after(1)
    print(L1)
    print(L2)

#%%
    L = SLinkedList()
    L.add_start(6)
    L.add_start(5)
    L.add_start(2)
    L.add_start(4)
    L.add_start(1)
    L.add_start(3)
    tmp = L.head
    a_list = []
    while tmp:
        a_list.append(tmp.data)
        tmp = tmp.next
    a_list.sort()
    new_list = SLinkedList()
    for item in a_list:
        new_list.add_start(item)
    print(L)
    print(new_list)




