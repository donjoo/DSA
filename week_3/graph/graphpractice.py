def add_node(v):
    global node_count
    if v in nodes:
        print(v,'is present')
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
        print('node not present')
    elif v2 not in nodes:
        print('node not present')
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2]=1
        graph[index2][index1]=1

def add_edge(v1,v2):
    if v1 not in nodes:
        print('notttttt')
    elif v2 not in nodes:
        print('notttttttt')
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1
        graph[index1][index2] = 1



def delete_node(v):
    global node_count
    if v not in nodes:
        print('fjvnf')
    else:
        index1 = nodes.index(v)
        node_count -= 1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)


def delete_edge(v1,v2):
    if v1 not in nodes:
        print('motttt')
    elif v2 not in nodes:
        print('fvffv')
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2]=0
        graph[index2][index1]=0


def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=' ')
        print()










nodes = []
graph=[]
node_count = 0
print("before adding")
print(nodes)
print(graph)
add_node("A")
add_node("A")
add_node("B")
add_node("V")
add_edge("A",'B')
add_edge("A",'V') 

# delete_node('B')
# delete_edge('A','V')
print("after adding nodes")
print("nodes",nodes)
print("graph",graph)
print_graph()