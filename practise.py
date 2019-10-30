
def create_graph(num_verti, edges):
    G = {}
    for i in range(num_verti):
        G[i] = set()
    for edge in edges:
        G[edge[0]].add(edge[1])
        G[edge[1]].add(edge[0])
    return G

def BFS(graph, source):
    marked = {vert:False for vert in graph}
    path_to = {vert:None for vert in graph}
    dist_to = {vert:None for vert in graph}
    marked[source] = True
    dist_to[source] = 0
    queue = [source]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if not marked[w]:
                marked[w] = True
                dist_to[w] = dist_to[v] + 1
                path_to[w] = v
                queue.append(w)
    return marked, dist_to, path_to





#%%
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']),
         'G': set()}

marked, dist_to, path_to = BFS(graph, 'A')
marked
dist_to
path_to