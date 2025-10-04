'''



🌳 What is a Tree?

A tree is a non-linear hierarchical data structure made up of nodes, where:

    The top node is called the root.

    Every node can have zero or more children.

    There's exactly one path between any two nodes (no cycles).



🔑 Basic Terminology
Term	                Description
Node	                Each element in the tree
Root	                The top-most node (only one root)
Parent	                A node that has one or more children
Child	                A node that descends from another node
Leaf	                A node with no children
Edge	                Connection between nodes
Height	                Max depth from root to any leaf
Depth	                Distance from the root to that node
Subtree	                A tree formed from any node and its descendants
Siblings	            Nodes with the same parent
Level	                The layer of nodes at a certain depth (root = level 0)









Classification of Trees – Based on Structure & Node Constraints

🔹 1. General Tree

    Each node can have any number of children.

    No constraint on number of children.

    Example: A file system (folder can have many subfolders).

        A
      / | \
     B  C  D
           |
           E

🔹 2. Binary Tree

    Each node has at most 2 children.

    Common types of tree used in algorithms.

        A
       / \
      B   C

🔹 3. Full Binary Tree

    Every node has either 0 or 2 children.

    No node has only 1 child.

        A
       / \
      B   C
     / \
    D   E

🔹 4. Perfect Binary Tree

    A full binary tree where all leaves are at the same level.

    All internal nodes have exactly 2 children.

        A
       / \
      B   C
     / \ / \
    D  E F  G

🔹 5. Complete Binary Tree

    All levels are completely filled except possibly the last,
    and all nodes in the last level are as far left as possible.

        A
       / \
      B   C
     / \  /
    D  E F

🔹 6. Balanced Binary Tree

    A binary tree where the height difference between left and right 
    subtrees of any node is not more than 1.

    Used to maintain search performance.

Example: AVL Tree, Red-Black Tree

        A
       / \
      B   C
     /
    D

🔹 7. Degenerate Tree / Skewed Tree

    A tree where each parent has only one child, making it like a linked list.

    Can be left-skewed or right-skewed.

Left-skewed:

    A
   /
  B
 /
C

Right-skewed:

A
 \
  B
   \
    C

🔹 8. N-ary Tree

    Each node can have at most N children.

    Generalization of a binary tree.

E.g., In a 3-ary tree:

    A
  / | \
 B  C  D

🔹 9. Binary Search Tree (BST)

    A binary tree with the following property:

        Left child < Parent < Right child

    Helps in fast search, insertion, and deletion.

      8
     / \
    4   10
   / \
  2   6

🧠 Summary Table
Tree Type	            Node Constraint	                    Use Case
General Tree	        Any number	                        File Systems
Binary Tree	            ≤ 2 children	                    Tree basics
Full Binary	            0 or 2 children	                    Strict tree structure
Perfect Binary	        Full + All leaves same level	    Ideal structure
Complete Binary	        Filled left to right	            Heaps
Balanced Binary	        Height difference ≤ 1	            AVL, Red-Black Trees
Degenerate Tree	        One child only	                    Worst-case BST
N-ary Tree	            Up to N children	                Game trees, Trie
BST	                    Left < Root < Right	                Efficient search




✅ How to Present in a Review

    "There are multiple types of trees classified based on node constraints.

        A general tree allows any number of children.

        A binary tree limits children to two.

        A full binary tree ensures every node has either 0 or 2 children.

        A perfect binary tree is a full tree with all leaves at the same depth.

        A complete binary tree fills levels left to right.

        A balanced tree ensures optimal height for performance.

        A skewed tree resembles a linked list.

        A BST applies ordering to enable fast operations.

    These distinctions are essential in choosing the right structure for a problem, especially when performance matters."







🔸 Classification based on node degree (branching factor)
Tree Type	Classification Based On
Binary Tree	Maximum 2 children per node
Ternary Tree	Maximum 3 children per node
K-ary Tree	Maximum K children per node
Threaded binary tree













'''



# Simple generic tree
    #      A
    #    / | \
    #   B  C  D
    #  / \
    # E   F



# output
# A
#   B
#      E
#      F
#   C
#   D
# 

class TreeNode:                                           
                                                             
    def __init__(self,data):                              
        self.data = data                                     
        self.children = []
        
    def add_child(self,child_node):
        self.children.append(child_node)
        
        
    def print_tree(self, level=0):
        print(" " * level * 2 + str(self.data))
        for child in self.children:
            child.print_tree(level +1)
            
root = TreeNode("A")
b = TreeNode('B')
c = TreeNode('C')
d = TreeNode('D')
e = TreeNode('E')
f = TreeNode('F')

root.add_child(b)
root.add_child(c)
root.add_child(d)
b.add_child(e)
b.add_child(f)

root.print_tree()

