def add_node(v):
    if v in graph:
        print(v,'pres')
    else:
        graph[v] = []




def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,'vvv')
    elif v2 not in graph:
        print(v2,'fff')
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


    
def DFS(node,visited,graph):
    if node not in graph:
        print(node,'not present')
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS[i,visited,graph]


from collections import deque

def bfs(graph,start_vertex):
    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)

    while queue:
        Vertex = queue.popleft()
        print(Vertex,end=' ')

        for neighbour in graph[Vertex]:
            if neighbour not in visited:
                visited.add(Vertex)
                queue.append(neighbour)



graph = {}
visited = set()