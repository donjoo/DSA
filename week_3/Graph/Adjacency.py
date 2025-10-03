class Graph:
    
    def __init__(self,directed = False):
        self.directed = directed
        self.adj_list = dict()
        
    def __repr__(self):
        graph_str = ""
        for node , neighbour in self.adj_list.items():
            graph_str += f"{node} --> {neighbour}"
        return graph_str
        
    def add_node(self,node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("node already exists")
            
    def remove_node(self,node):
        if node not in self.adj_list:
            raise ValueError("node doesnt exists")
        for neighbours in self.adj_list.values():
            neighbours.discard(node)
        del self.adj_list[node]
        
    def add_edge(self,from_node, to_node, weighted = None):
        if not from_node in self.adj_list:
            self.adj_list[from_node] = set()
        if not to_node in self.adj_list:
            self.adj_list[to_node] = set()
        if  weighted is None:
            self.adj_list[from_node].add(to_node)
            if not self.directed:
                self.adj_list[to_node].add(from_node)
        else:
            self.adj_list[from_node].add((to_node,weighted))
            if not self.directed:
                self.adj_list[to_node].add((from_node,weighted))
                
    def remove_edge(self,from_node,to_node):
        if  from_node in self.adj_list:
            if  to_node in self.adj_list[from_node]:
               self.adj_list[from_node].remove(to_node)
            else:
                 raise ValueError("edge doesnt exists")
            if not self.directed:
                self.adj_list[to_node].remove(from_node)
        else:
            raise ValueError("edge doest exists")
            
    def get_neighbours(self,node):
        return self.adj_list[node]
    
    def has_node(self,node):
        return node in self.adj_list
        
    def has_edge(self,from_node, to_node):
        if from_node in self.adj_list:
            return to_node in self.adj_list[from_node]
        return False
    def get_node(self):
        return self.adj_list.keys()
    def get_edges(self):
        edges = []
        for from_node, neighbours in self.adj_list.items():
            for to_node in neighbours:
                edges.append((from_node,to_node))
        return edges
    def bfs(self,start):
        visited = set()
        queue = [start]
        order = []
        
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbours = self.adj_list[node]
                for neighbour in neighbours:
                    if isinstance(neighbour,tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        queue.append(neighbour)
        return order
        
    def dfs(self,start):
        visited = set()
        stack = [start]
        order = []
        
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
               
                for neighbour in sorted(self.adj_list[node], reverse=True):
                    if isinstance(neighbour,tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        stack.append(neighbour)
        return order
         

           
    def shortest_path_unweighted(self,start, target):
        from collections import deque 
        if not start in self.adj_list or target not in self.adj_list:
            raise ValueError("nt present")
        
        visited = set()
        queue = deque([(start,[start])])
        
        
        while queue:
            node,path = queue.popleft()
            if node == target:
                return path
            if node not in visited:
                visited.add(node)
                for neighbour in self.adj_list[node]:
                    if isinstance(neighbour,tuple):
                        neighbour = neighbour[0]
                    if not neighbour in visited:
                        queue.append((neighbour, path + [neighbour]))
        return None
         
g = Graph()
g.add_node("A")
g.add_node("B")
g.add_edge("A", "B")
g.add_edge("A", "C")
print(g)

print("BFS:", g.bfs("A"))
print("DFS:", g.dfs("A"))
               