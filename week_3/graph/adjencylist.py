def add_node(v):
    if v in graph:
        print(v,"is present in the graph")
    else:
        graph[v]=[]

# undirected and unweighted
# def add_edge(v1,v2):
#     if v1 not in graph:
#         print(v1,"not present n graph")
#     elif v2 not in graph:
#         print(v2,"is not present in the graph")
#     else:
#         graph[v1].append(v2)
#         graph[v2].append(v1)


# weighted and undirected
def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1,"not present n graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        list1 = [v2,cost]
        list2 = [v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)


# directed weighted
# def add_edge(v1,v2,cost):
#     if v1 not in graph:
#         print(v1,"not present n graph")
#     elif v2 not in graph:
#         print(v2,"is not present in the graph")
#     else:
#         list1 = [v2,cost]
#         graph[v1].append(list1)


# directed unweighted
# def add_edge(v1,v2):
#     if v1 not in graph:
#         print(v1,"not present n graph")
#     elif v2 not in graph:
#         print(v2,"is not present in the graph")
#     else:
#         graph[v1].append(v2)

# directed and unweighted
# def delete_node(v):
#     if v not in graph:
#         print(v,'is not present in the graph')
#     else:
#         graph.pop(v)
#         for i in graph:
#             list1 = graph[i]
#             if v in list1:
#                 list1.remove(v)


# undirecteed and  unweighted
def delete_node(v):
    if v not in graph:
        print(v,'is not present in the graph')
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            for j in list1:
                if v == j[0]:
                    list1.remove(j)
                    break


# delete edge# delete edge
# delete edge# delete edge

# unweighted and undirected
# def delete_edge(v1,v2):
#     if v1 not in graph:
#         print(v1,"is not in the graph")
#     elif v2 not in graph:
#         print(v2,"not present in the graph")
#     else:
#         if v2 in graph[v1]:
#             graph[v1].remove(v2)
#             graph[v2].remove(v1) 





# unweighted and directed
# def delete_edge(v1,v2):
#     if v1 not in graph:
#         print(v1,"is not in the graph")
#     elif v2 not in graph:
#         print(v2,"not present in the graph")
#     else:
#         if v2 in graph[v1]:
#             graph[v1].remove(v2)




# weighted and undirected
def delete_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1,"is not in the graph")
    elif v2 not in graph:
        print(v2,"not present in the graph")
    else:
        temp = [v1,cost]
        temp1 = [v2,cost]
        if temp1 in graph[v1]:
            graph[v1].remove(temp1)
            graph[v2].remove(temp)


graph = {}
add_node('A')
add_node('B')
add_node('C')

# add_edge('A','B')
# add_edge('A','C')
add_edge('A','B',7)
add_edge('A','C',9)
print(graph)
# delete_node('C')
delete_edge('A','C',9)
print(graph)