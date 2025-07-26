'''
✅ 1. What is a Binary Tree?

A binary tree is a non-linear hierarchical data structure where each node has at most 2 children.

Each node has:

    A value

    A left child

    A right child


✅ Types of Binary Trees
Type	Description
Full Binary Tree	Every node has 0 or 2 children

Complete Binary Tree	All levels filled left to right, last level may not be full

Perfect Binary Tree	All levels fully filled

Balanced Binary Tree	Height difference between left & right ≤ 1

Degenerate Tree	 Each parent has only 1 child (like a linked list)



🧮 Time Complexities (Balanced Binary Tree)
Operation	Time Complexity
Insert	O(log n)
Delete	O(log n)
Search	O(log n)
📌 Worst case (if skewed): O(n)
That’s why we use balanced trees like AVL for performance.


🎯 When to Use Binary Trees

    Efficient search, insert, delete

    Representing expression trees

    Parsing and syntax trees in compilers

    File system structure (partial)

    Binary Heaps for priority queues



🧪 Interview Questions Based on Binary Trees

    Check if a binary tree is balanced.

    Convert binary tree to doubly linked list.

    Find LCA (Lowest Common Ancestor).

    Print tree level-by-level.

    Diameter of a binary tree.

    Serialize and deserialize a tree.

'''
'''

        A
       / \
      B   C
     / \   \
    D   E   F
'''


from collections import deque


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
        
        
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=' ')
        inorder(node.right)

def preorder(node):
    if node:
        print(node.value,end=' ')
        preorder(node.left)
        preorder(node.right)
        
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end= '')

def level_order(root):
    if not root:
        return 
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.value, end = ' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
            

#  Inorder Traversal (Iterative)

def inorder_iterative(root):
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        print(curr.value, end= ' ')
        curr = curr.right
        
# Preorder Traversal (Iterative)

def preorder_iterative(root):
    if not root:
        return 
    stack = [root]
    while stack:
        node.stack.pop()
        print(node.value, end=' ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# Post_order (iterative)

def postorder_iterative(root):
    if not root:
        return
    stack1 = [root]      
    stack2 = []       
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        print(stack2.pop().value, end=' ')
        

def height(node):
    if not node:
        return -1
    return 1 + max(height(node.left), height(node.right))

def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)
    
def count_leaf_nodes(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    return count_leaf_nodes(node.left) + count_leaf_nodes(node.right)
    
    
def diameter(root):
    def helper(node):
        if not node:
            return (0,0)
        lh,ld = helper(node.left)
        rh,rd = helper(node.right)
        current_diameter = lh + rh
        return (1 + max(lh,rh), max(ld,rd, current_diameter))
    return helper(root)[1]
    
def mirror_tree(node):
    if node:
        node.left, node.right = node.right,node.left
        mirrot_tree(node.left)
        mirror_tree(node.right)
    

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')


print('inorder')
inorder(root)
print()

print('preorder')
preorder(root)


print('\npostorder')
postorder(root)


print('\nlevel order')
level_order(root)

print('height')
print(height(root))

print('diameter')
print(diameter(root))