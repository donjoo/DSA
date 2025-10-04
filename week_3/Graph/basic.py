'''

🌱 What is a Graph?

A Graph is a collection of:

    Vertices (nodes) — entities

    Edges — connections between vertices

Mathematically:
G = (V, E)
Where:

    V = set of vertices

    E = set of edges (pairs of vertices)


 Graph Terminology

    Vertex (node) → A point in the graph

    Edge → Connection between two vertices

    Adjacent vertices → Vertices connected by an edge

    Degree → Number of edges connected to a vertex

        In-degree (incoming edges)

        Out-degree (outgoing edges)

    Path → Sequence of vertices connected by edges

    Cycle → Path that starts and ends at the same vertex

    Connected graph → Path exists between every pair of vertices




| Type                   | Description                                    |
| ---------------------- | ---------------------------------------------- |
| **Directed** (Digraph) | Edges have a direction                         |
| **Undirected**         | Edges have no direction                        |
| **Weighted**           | Edges have weights/costs                       |
| **Unweighted**         | All edges have equal cost                      |
| **Cyclic**             | Has at least one cycle                         |
| **Acyclic**            | No cycles (e.g., DAG - Directed Acyclic Graph) |
| **Connected**          | Every vertex reachable from another            |
| **Disconnected**       | Some vertices not connected                    |




Graph Storage Methods
1️⃣ Adjacency List

    What: Stores each vertex and a list of its neighbors.

    Implementation: Dictionary → linked list (or array) of connected vertices.

    Time complexity:

        Check adjacency → O(V) in worst case for linked list

        Traversal → O(V + E)

    Space complexity: O(V + E)
    (V = vertices, E = edges)

📌 Example as Linked List:

graph = {
    0: [1, 4],
    1: [0, 2, 3],
    2: [1],
    3: [1, 4],
    4: [0, 3]
}

Pros:

    Efficient for sparse graphs

    Saves memory compared to adjacency matrix

Cons:

    Checking if an edge exists may take O(V)



---------------------
2️⃣ Adjacency Matrix

    What: A 2D array where matrix[i][j] = 1 (or weight) if there’s an edge, else 0 (or ∞ for weighted graphs).

    Time complexity:

        Check adjacency → O(1)

        Traversal → O(V²)

    Space complexity: O(V²)

📌 Example:
   0 1 2 3
0: 0 1 0 1
1: 1 0 1 1
2: 0 1 0 0
3: 1 1 0 0

Pros:

    Fast adjacency check

    Simple implementation

Cons:

    Wastes space for sparse graphs

3️⃣ Graph Traversal

Breadth-First Search (BFS)

    Level-by-level

    Uses a queue

    O(V + E) time

Depth-First Search (DFS)

    Goes deep before backtracking

    Uses recursion or stack

    O(V + E) time

Practice:

    BFS and DFS on adjacency list

    Detect if a graph is connected

    Detect cycles





--------------------------------------------------------------------


| Feature        | BFS                               | DFS                              |
| -------------- | --------------------------------- | -------------------------------- |
| Data Structure | Queue (FIFO)                      | Stack (LIFO) / Recursion         |
| Order          | Level-by-level                    | Deep before backtracking         |
| Use Case       | Shortest path in unweighted graph | Path existence, topological sort |
| Space          | O(V)                              | O(V)                             |






'''

from collections import defaultdict


# 2️⃣ Graph Class Using Adjacency List
class Graph:
    
    def __init__(self,directed=False):
        self.graph = defaultdict(list)
        self.directed = directed
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)
            
            
    def display(self):
        for vertex in self.graph:
            print(vertex,'->',self.graph[vertex])
            
g = Graph(directed=False)


g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")

g.display()






# 4️⃣ Graph Using Adjacency Matrix
class GraphMatrix:
    
    def __init__(self,vertices):
        self.v = vertices
        self.matrix = [[0] * vertices for _ in range(vertices)]
        
    def add_edge(self,u,v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1
    
    def display(self):
        for row in self.matrix:
            print(row)
            
gm = GraphMatrix(4)  # 4 vertices: 0,1,2,3
gm.add_edge(0, 1)
gm.add_edge(0, 2)
gm.add_edge(1, 3)
gm.display()
 



