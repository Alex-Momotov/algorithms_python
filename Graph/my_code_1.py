
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


def create_graph(num_nodes, edges):
    G = {}
    for i in range(num_nodes):
        G[i] = []
    for edg in edges:
        G[edg[0]].append(edg[1])
        G[edg[1]].append(edg[0])
    return G

def BFS(graph, source):
    marked = {node:False for node in graph} # Keep track of visited nodes
    dist_to = {node:-1 for node in graph}   # -1 means node is unreachable
    path_to = {node:-1 for node in graph}   # -1 means node is unreachable
    marked[source] = True                   # Mark source as visited
    dist_to[source] = 0                     # Distance to source is zero
    queue = Queue()                         # Create queue
    queue.enqueue(source)                   # Enqueue source node
    while len(queue) != 0:                  # While queue is not empty
        v = queue.dequeue()                 # Dequeue a vertex 'v'
        for n in graph[v]:
            if not marked[n]:
                queue.enqueue(n)
                marked[n] = True
                dist_to[n] = dist_to[v] + 1
                path_to[n] = v
    return marked, dist_to, path_to

def DFS(graph, start, visited=None):
    """Recursive definition of DFS"""
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        DFS(graph, next, visited)
    return visited

def DFS_(graph, start):
    """Iterative definition of DFS"""
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

#%%
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

BFS(graph, 'A')
