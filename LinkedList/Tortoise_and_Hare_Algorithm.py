import sys
sys.path.append(r"C:\Users\Sasha\Coding\Algorithms and Data Structures\Algorithms in Python\LinkedList")
from SLinkedList import SLinkedList


def has_cycle(head):
    """Floyd's Cycle-Finding Algorithm.
    Also known as Tortoise and Hare Algorithm."""
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


L = SLinkedList()
for i in range(1,8): L.add_start(i)
tmp = L.head
while tmp.next: tmp = tmp.next
tmp.next = L.head.next.next.next.next
print(has_cycle(L.head))



