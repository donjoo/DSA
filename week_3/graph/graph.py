# connected
# adjency matrix
# directed or un directed
# weighted or unweighted

def add_node(v):
    global node_count
    if v in nodes:
        print(v,'is present in the graph')
    else:
        node_count = node_count + 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)


def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print(v1,'not present in graph')
    elif v2 not in nodes:
        print(v2,'not present in graph')
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1
        # graph[index2][index1]=cost



# undirected 
def delete_node(v):
    global node_count
    if v not in nodes:
        print(v,'if not present in the graph')
    else:
        index1 = nodes.index(v)
        node_count = node_count-1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)


def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1,'is not present in graph')
    elif v2 not in nodes:
        print(v2,'is not presemt in graph')
    else:
        index1 =nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2] = 0
        graph[index2][index1] = 0



# directed
def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1,'not present')
    elif v2 not in nodes:
        print(v2,'not present')
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        # graph[index2][index1] = 0


     



def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"<3"),end=' ')
        print()

nodes  = []
graph = []
node_count = 0
print("before adding")
print(nodes)
print(graph)
add_node("A")
add_node("A")
add_node("B")
add_node("V")
add_edge("A",'B',10)
add_edge("A",'V',4) 

# delete_node('B')
# delete_edge('A','V')
print("after adding nodes")
print("nodes",nodes)
print("graph",graph)
print_graph()