'''
🔹 What is a Trie?

A Trie (prefix tree) is a tree data structure for storing strings where:

    Each node represents a single character.

    Paths from the root represent prefixes of words.

    Words are terminated using a special marker (boolean flag or terminator char).



6️⃣ Suffix Tree vs Trie

    Prefix Tree (Trie): Stores words so that each path from root is a prefix.

    Suffix Tree: Stores all possible suffixes of a word/string.

        Useful for substring search

        Takes more space than a prefix tree


A terminator character marks the end of a valid word in a Trie. Instead of storing a special 
character like '\0', most Trie implementations use a boolean flag is_end on the last node of a
 word. This allows distinguishing between words that share prefixes, like 'car' and 'carpet'.




1️⃣ Compressed Trie

A Compressed Trie is an optimized version of a standard Trie where:

    Instead of storing one character per node, we merge chains of single-child nodes into a single node with a substring.

📌 Why?

    Standard Tries waste space when many nodes have only one child.

    Compression saves memory and speeds up traversal.

✅ Benefits

    Less memory usage

    Faster traversal (fewer nodes to visit)

root
 └── "ca"
       ├── "r"* 
       └── "t"*



---------------

2️⃣ Radix Tree (Patricia Trie)

A Radix Tree (or Patricia Trie — Practical Algorithm to Retrieve Information Coded in Alphanumeric) is a type of compressed trie that:

    Merges single-child paths like compressed tries

    Stores entire strings on edges instead of one character per node

    Often used for string keys in dictionaries/maps

    Can also store binary strings (bitwise Patricia Tree)


✅ Benefits

    Saves space by compressing long single-branch paths

    Lookup still O(m) where m = length of key

    Great for prefix-based storage with less overhead

root
 ├── "b"
 │    ├── "ear"*
 │    ├── "ell"*
 │    └── "id"*
 └── "s"
      ├── "ell"*
      └── "tock"*



| Feature      | Compressed Trie                   | Radix Tree (Patricia Trie)                  |
| ------------ | --------------------------------- | ------------------------------------------- |
| Optimization | Merges single-child chains        | Merges chains + stores substrings on edges  |
| Space Usage  | Lower than normal trie            | Even lower (fewer nodes, more compact)      |
| Storage Type | Char nodes merged into substrings | Edge-based substrings                       |
| Use Cases    | Autocomplete, dictionaries        | Routing tables, dictionaries, text indexing |












'''








class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0
            char = word[depth]
            if char not in node.children:
                return False
            should_delete = _delete(node.children[char], word, depth+1)
            if should_delete:
                del node.children[char]
                return not node.is_end and len(node.children) == 0
            return False
        _delete(self.root, word, 0)
