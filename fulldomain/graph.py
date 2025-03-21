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


    

def delete_node(v):
    global node_count
    if v not in nodes:
        print(v,'not present')
    else:
        index1 = nodes.index(v)
        node_count = node_count - 1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

        
def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1,'not')
    elif v2 not in nodes:
        print(v2,'not in graph')
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        graph[index1][index2] = 0






nodes =[]
graph = []