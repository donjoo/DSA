def add_node(v):
    if v in graph:
        print(v,'is already present in the graph')
    else:
        graph[v] = []


def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,'is ot present in the graph')
    elif v2 not in graph:
        print(v2,'is not present in the graph')
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


def DFS(node,visited,graph):
    if node not in graph:
        print("Node is not present in the graph")
        return 
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)


from collections import deque

def bfs(graph, start_vertex):
    visited = set()          # To keep track of visited vertices
    queue = deque([start_vertex])  # Initialize the queue with the start vertex
    visited.add(start_vertex) # Mark the start vertex as visited

    while queue:
        vertex = queue.popleft()  # Dequeue a vertex from the queue
        print(vertex, end=' ')    # Process the vertex

        for neighbor in graph[vertex]:  # For each adjacent vertex
            if neighbor not in visited: # If the neighbor hasn't been visited
                visited.add(neighbor)   # Mark it as visited
                queue.append(neighbor)





visited = set()
graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")


add_edge("A","B")
add_edge("B","E")
add_edge("A","C")
add_edge("A","D")
add_edge("B","D")
add_edge("C","D")
add_edge("E","D")
print(graph)
print('ffffffffffffffffff')
DFS("C",visited,graph)
bfs(graph,'A')