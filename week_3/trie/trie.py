class Node:
  def __init__(self):
    self.children={}
    self.iscomplete=False

class Trie:
  def __init__(self):
    self.root=Node()
   
  def insert(self,word):
    node=self.root
    for char in word:
      if char not in node.children:
        node.children[char]=Node()
      node=node.children[char]
    node.iscomplete=True
    
  def search(self,word):
    node=self.root
    for char in word:
      if char not in node.children:
        return False
      node=node.children[char]
    return node.iscomplete
      
  def starts_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
      
  def delete(self,word):
    self.delete_helper(self.root,word,0)
    
  def delete_helper(self,node,word,index):
    if index==len(word):
      if node.iscomplete:
        node.iscomplete=False
      return
    
    char=word[index]
    if char not in node.children:
      return
    
    child_node=node.children[char]
    self.delete_helper(child_node,word,index+1)
    if not child_node.iscomplete and not child_node.children:
      del node.children[char]
      
trie=Trie()
words = ["apple", "appetizer", "banana", "bat", "batman"]
for word in words:
  trie.insert(word)
  
  
print("Prefix = ",trie.starts_with_prefix("ap"))
print("Search = ",trie.search("banana"))
trie.delete("banana")
print("Search after deletion = ",trie.search("banana"))
# print(trie.root)