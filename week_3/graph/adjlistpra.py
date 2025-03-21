def add_node(v):
    if v in graph:
        print("is present")
    else:
        graph[v]=[]

def add_edge(v1,v2,cost):
    if v1 not in graph:
        print("not present")
    elif v2 not in graph:
        print(v2,'not present')
    else:
        list1 = [v2,cost]
        list2 = [v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)


def delete_node(v):
    if v not in graph:
        print(v,'is not present in the graph')
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            for j in list1:
                if v == j[0]:
                    list1.removes(j)
                    break

def delete_node(v):
    if v not in graph:
        print('noffjm')
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            for j in list1:
                if v == j[0]:
                    list1.remove(j)
                    break



def delete_edge(v1,v2,cost):
    if v1 not in graph:
        print('fvvvv')
    elif v2 not in graph:
        print('fjkf')
    else:
        temp = [v1,cost]
        temp1 = [v2,cost]
        if temp1 in graph[v1]:
            graph[v1].remove(temp1)
            graph[v2].remove(temp)

            




















graph = {}
