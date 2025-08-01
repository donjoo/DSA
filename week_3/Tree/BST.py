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






Use Case	                                Why BST Works Well

Fast search/insert/delete	                O(log n) time (if balanced)
Sorted data traversal	                    Inorder gives sorted order
Range queries / top-K	                    Easily implemented with BST
Underlying for sets/maps	                Java/C++ STL use balanced BSTs
Expression parsing	                        Used in compilers
Auto-complete, prefix matching	            Combined with strings and Tries
Memory-efficient structures	                With AVL/Splay trees



🧠 Bonus: When not to use BST?
Situation	                    Better Alternative
You need hash-based access	    Use HashMap / dict
You need prefix search	        Use Trie
You need fast disk access	    Use B-Tree
You need min/max in O(1)	    Use Heap






⚖️ What Is a Balanced Tree?

A Balanced Tree is a binary tree where the difference in height between the left and right subtree of any node is not more than 1.

    ✅ Balance condition:
    |height(left) - height(right)| ≤ 1 for every node


❌ What Is an Unbalanced Tree?

An Unbalanced Tree does not satisfy the balance condition.

    One subtree is significantly deeper than the other.

    Happens when nodes are inserted in sorted order in a normal BST.

🧠 Why Balance Matters?
Operation	Balanced Tree	Unbalanced Tree
Search	O(log n)	O(n)
Insert	O(log n)	O(n)
Delete	O(log n)	O(n)

✅ Balanced trees ensure fast operations.
❌ Unbalanced trees cause performance issues.
🧱 Balanced Trees Examples
Tree Type	Description
AVL Tree	Self-balancing BST using rotations
Red-Black Tree	Used in Java’s TreeMap, C++ STL (set/map)
B-Trees	Used in databases, optimized for disk storage
Splay Tree	Self-adjusting BST
🔄 How Trees Are Balanced?
✅ By using Rotations after insert/delete:

    Left Rotation

    Right Rotation

    Left-Right / Right-Left Rotation (in AVL Trees)

They restructure the tree to restore the balance condition.
📌 Analogy

    Balanced Tree: Books stored on well-organized shelves → easy to find one quickly

    Unbalanced Tree: Books thrown in a vertical stack → slow, top-to-bottom search

🚀 Summary Table
Feature	Balanced Tree	Unbalanced Tree
Height	log₂(n)	up to n (in worst case)
Operations	O(log n)	O(n)
Efficiency	High	Low
Structure	Evenly distributed	Skewed to one side
Common Examples	AVL, Red-Black, B-Tree	Plain BST (inserting sorted data)
Self-adjusting	Yes (with rotations)	No
✅ Interview Tip:

    ❓Q: How do you make sure a BST stays efficient?
    ✅ "By keeping it balanced using AVL or Red-Black Tree to ensure operations stay O(log n)."





Properties of BST
🧠 Summary Table
Property	                    Description
Left < Root < Right	            Core rule that defines BST
No Duplicates	                Usually enforced for clean ordering
Recursive BSTs	                Subtrees are themselves BSTs
In-Order = Sorted	            Output is ascending if tree is valid
Search/Insert/Delete	        O(log n) average, O(n) worst-case
Min/Max	                        Found by traversing left/right edge
Balanced BSTs	                Keep operations fast by maintaining low height
Violations	                    Any node breaking the rule invalidates BST


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


    # Check if Valid BST
    def is_valid_bst(self):
        def is_valid(node, low, high):
            if not node:
                return True
            if not (low < node.key < high):
                return False
            return is_valid(node.left, low, node.key) and is_valid(node.right, node.key, high)

        return is_valid(self.root, float('-inf'), float('inf'))

    # Lowest Common Ancestor
    def lowest_common_ancestor(self, n1, n2):
        return self._lca(self.root, n1, n2)

    def _lca(self, root, n1, n2):
        if not root:
            return None
        if n1 < root.key and n2 < root.key:
            return self._lca(root.left, n1, n2)
        if n1 > root.key and n2 > root.key:
            return self._lca(root.right, n1, n2)
        return root

    # Ceil in BST
    def find_ceil(self, key):
        root = self.root
        ceil = -1
        while root:
            if root.key == key:
                return root.key
            if key < root.key:
                ceil = root.key
                root = root.left
            else:
                root = root.right
        return ceil

    # Floor in BST
    def find_floor(self, key):
        root = self.root
        floor = -1
        while root:
            if root.key == key:
                return root.key
            if key > root.key:
                floor = root.key
                root = root.right
            else:
                root = root.left
        return floor

    # Kth smallest element
    def kth_smallest(self, k):
        res = []
        self._inorder(self.root, res)
        if 0 < k <= len(res):
            return res[k-1]
        return None

    # Kth largest element
    def kth_largest(self, k):
        res = []
        self._reverse_inorder(self.root, res)
        if 0 < k <= len(res):
            return res[k-1]
        return None

    def _reverse_inorder(self, root, res):
        if root:
            self._reverse_inorder(root.right, res)
            res.append(root.key)
            self._reverse_inorder(root.left, res)


# 🌿 Test the BST
bst = BST()
for num in [15, 10, 20, 8, 12, 17, 25]:
    bst.insert(num)

print("Inorder:", bst.inorder())
print("Search 12:", bst.search(12) is not None)
print("Level Order:", bst.level_order())
print("Kth Smallest (3rd):", bst.kth_smallest(3))
print("Ceil of 13:", bst.find_ceil(13))
print("Floor of 13:", bst.find_floor(13))
print("LCA of 8 and 12:", bst.lowest_common_ancestor(8, 12).key)
print("Valid BST:", bst.is_valid_bst())