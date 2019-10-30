
"""This implementation from Python standard library uses doubly linked list behind the scenes."""

from collections import deque
Q = deque()     # Create a queue
Q.append(1)     # .push()
Q.pop()         # .pop()
Q[-1]           # .peek()
len(Q)          # .size()
len(Q) == 0     # .is_empty()
