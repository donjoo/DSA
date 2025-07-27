'''
🌲 What is a Binary Search Tree (BST)?

A BST is a special kind of Binary Tree that maintains a specific order:
✅ BST Property:

For every node:

    All values in the left subtree are less than the node.

    All values in the right subtree are greater than the node.



🌳 1. BST vs Binary Tree (BT)
Feature	            Binary Tree (BT)	Binary Search Tree (BST)
Node Children	    Max 2	                Max 2
Value Order	        No specific order	    Left < Root < Right
Search Efficiency	O(n)	                O(log n) (in balanced BST)
Use Case	        General storage	        Fast search, insertion, deletion



✅ 2. Uses of BST

    Faster search, insert, delete than regular BT

    Used in:

        Maps, Sets, Dictionaries

        DB Indexing

        Memory management

        Range queries

        Auto-suggestion, autocomplete



🌳 What’s a Balanced BST?

A Balanced BST is a binary search tree where:

    ✅ The height difference between the left and right subtree of every node is at most 1.

This means:

    Tree is not skewed.

    Depth of all leaf nodes is roughly equal.

    Operations like insert, delete, search are O(log n)

🌴 What’s an Unbalanced BST?

An Unbalanced BST does not maintain the balance condition.
It can become skewed if values are inserted in sorted order.

Result:

    Tree behaves like a linked list.

    Operations degrade to O(n) instead of O(log n).



✅ 4. Properties of BST

    Left subtree values < node value

    Right subtree values > node value

    No duplicates (commonly assumed)

    Inorder traversal gives sorted values





'''



class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insertion
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root

    # Search
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    # In-order Traversal (DFS)
    def inorder(self):
        res = []
        self._inorder(self.root, res)
        return res

    def _inorder(self, root, res):
        if root:
            self._inorder(root.left, res)
            res.append(root.key)
            self._inorder(root.right, res)

    # Pre-order Traversal (DFS)
    def preorder(self):
        res = []
        self._preorder(self.root, res)
        return res

    def _preorder(self, root, res):
        if root:
            res.append(root.key)
            self._preorder(root.left, res)
            self._preorder(root.right, res)

    # Post-order Traversal (DFS)
    def postorder(self):
        res = []
        self._postorder(self.root, res)
        return res

    def _postorder(self, root, res):
        if root:
            self._postorder(root.left, res)
            self._postorder(root.right, res)
            res.append(root.key)

    # BFS / Level-order Traversal
    def level_order(self):
        from collections import deque
        res = []
        if not self.root:
            return res
        q = deque([self.root])
        while q:
            node = q.popleft()
            res.append(node.key)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res

    # Delete Node
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return None
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)
        return root

    def _min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current
