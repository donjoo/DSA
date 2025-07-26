'''



🌳 What is a Tree?

A tree is a non-linear hierarchical data structure made up of nodes, where:

    The top node is called the root.

    Every node can have zero or more children.

    There's exactly one path between any two nodes (no cycles).



🔑 Basic Terminology
Term	Description
Node	Each element in the tree
Root	The top-most node (only one root)
Parent	A node that has one or more children
Child	A node that descends from another node
Leaf	A node with no children
Edge	Connection between nodes
Height	Max depth from root to any leaf
Depth	Distance from the root to that node
Subtree	A tree formed from any node and its descendants
Siblings	Nodes with the same parent
Level	The layer of nodes at a certain depth (root = level 0)



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

