'''



🌲 AVL Tree — Balanced Binary Search Tree
AVL Tree is a self-balancing Binary Search Tree (BST) named after its 
inventors Adelson-Velsky and Landis.

✅ Key Properties

    It is a BST — so it follows the BST rule:

        Left subtree < Node < Right subtree

    It is balanced — so the height difference (balance factor) between left and right subtree of any node is at most 1

📐 Balance Factor

Balance Factor (BF) of a node:

BF = height(left subtree) - height(right subtree)

    Valid BF: -1, 0, +1

    If any node has BF not in this range, the tree is unbalanced and needs rotation


🔁 Types of Rotations (To Maintain Balance)
Case	Description	Rotation Required
LL	Left-Left (inserted in left of left child)	Right Rotation
RR	Right-Right (inserted in right of right child)	Left Rotation
LR	Left-Right (inserted in right of left child)	Left-Right Rotation
RL	Right-Left (inserted in left of right child)	Right-Left Rotation







🌳 Red-Black Tree (RBT)

A Red-Black Tree is a kind of self-balancing Binary Search Tree (BST) that maintains balance using color properties.

🔺 Red-Black Tree Rules:

    Every node is either red or black

    The root is always black

    All leaves (NIL/null nodes) are black

    Red nodes can’t have red children (no two reds in a row)

    Every path from a node to its descendant NIL nodes has the same number of black nodes (called black height)

🔄 Why is Red-Black Tree used?

    Ensures O(log n) time for search, insert, and delete.

    Balancing is more relaxed than AVL (fewer rotations).

    Useful when more inserts/deletes are expected (AVL is better for searches).

🔄 Rotations + Recoloring

Just like AVL trees, rotations are used:

    Left Rotation

    Right Rotation

But in RBTs, we also use recoloring to fix violations of red-black rules.


⚖️ AVL vs Red-Black Tree
Feature	AVL Tree	Red-Black Tree
Height Balance	Strict (BF = -1/0/1)	Relaxed (color-based)
Rotations	More frequent	Fewer rotations
Best For	Search-heavy apps	Insert/Delete-heavy apps
Complexity	O(log n)	O(log n)
🧠 How to Explain in a Review

    "A Red-Black Tree is a self-balancing binary search tree that uses color properties to ensure balance. It guarantees that the tree height remains logarithmic, ensuring O(log n) time for search, insertion, and deletion.
    It allows a bit more flexibility in balancing compared to AVL trees and balances itself using both rotations and recoloring to maintain five strict properties — like no two red nodes in a row and uniform black height on all paths."



🌲 What is a Prefix Tree (Trie)?

A Trie (pronounced "try") is a tree-based data structure used to efficiently store and retrieve keys in a dataset of strings, especially for prefix-based searching.

    📌 Each node represents a single character, and a path from the root to a node represents a prefix or a whole word.



🌳 What is an M-Way Search Tree?

An M-way search tree is a generalization of a binary search tree (BST) where each node can have up to M - 1 keys and M children.
An M-Way Search Tree is a generalization of a binary search tree, where each node can store up to M−1 keys and have M children. Keys are stored in sorted order, and children represent key ranges. This reduces the tree height and improves access time, especially for disk-based systems. M-Way trees form the basis of B-trees, which are widely used in databases and file systems for efficient indexing and search.

🧠 Why Use M-Way Trees?

As M increases:

    Tree becomes shorter → fewer levels to traverse

    ✅ More efficient disk access (used in database indexes)

That’s why B-trees and B+ trees, used in databases and file systems, are based on M-way search trees.

✅ In simple terms:

    BST: 1 key → 2 children

    M-way tree: Up to M−1 keys → Up to M children




------------------


🌳 B+ TREE (Variant of B-Tree)
✅ What is a B+ Tree?

A B+ Tree is an enhancement of the B-Tree with a key difference:

    All data is stored in the leaf nodes, and internal nodes only guide the search.


🔑 Key Properties of B+ Tree:
Property	Description
Internal nodes	Only store keys, not data
Leaf nodes	Store all data (and often in linked list form for range queries)
Uniform depth	Like B-tree, all leaves are at the same level
Range search	Faster due to linked leaves
🔄 How It Works

    Internal nodes are like indexes

    Leaf nodes are like pages containing actual records

    Insertion splits leaf nodes when full, possibly pushing keys to internal nodes







🧠 B+ Tree vs B-Tree – Comparison Table
Feature	B-Tree	B+ Tree
Stores data	In all nodes	Only in leaf nodes
Internal nodes	Store data & keys	Only store keys
Leaf node structure	No guaranteed linkage	Usually linked (doubly)
Range queries	Slower	Faster (sequential scan via linked leaves)
Search path	Ends at any node (data)	Always ends at leaf
Use case	General in-memory + disk use	Optimized for disk + range scan




🌳 What is a Merkle Tree?

A Merkle Tree, also called a Hash Tree, is a binary tree used to efficiently and securely verify the integrity of data.

    📌 Instead of storing values in the nodes, a Merkle Tree stores hashes of data. Each leaf node contains a hash of a data block, and each internal node contains the hash of the concatenation of its child nodes' hashes.

✅ Real-World Uses
Field	Usage
🌐 Blockchain	Transaction verification (e.g., Bitcoin, Ethereum)
💾 File storage	Verifying file integrity (e.g., IPFS, Git)
🧪 Security	Tamper detection and audit trails


🧪 Why Use Hashes?

    Tamper-proof: Changing a single bit in any block changes its hash → which changes the root

    Efficient verification: You don’t need the full data to verify a part, just the Merkle proof (a few sibling hashes)

A Merkle Tree is a binary tree where each leaf node contains the hash of a data block, and each internal node contains the hash of the concatenation of its child hashes. It's used for secure and efficient data verification.
In systems like blockchains, only the Merkle root is stored in the block header. To verify a transaction, we use a Merkle proof — a minimal set of sibling hashes — to recompute and compare the root.
This structure enables efficient O(log n) verification and tamper detection, even across large datasets





'''