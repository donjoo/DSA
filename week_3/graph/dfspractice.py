def add_node(v):
    if v in graph:
        print(v,'fef')
    else:
        graph[v]=[]

def add_edge(v1,v2):
    if v1 not in graph:
        print('kdjsf')
    elif v2 not in graph:
        print(v2,'dfkskj')
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)




def DFS(node,visited,graph):
    if node not in graph:
        print("node is not present")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)









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
DFS("A",visited,graph)