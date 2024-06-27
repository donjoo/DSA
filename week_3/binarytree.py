class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return 
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self,data):
        if self.key == data:
            print("node is found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in the tree")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("node is not present")

    def preorder(self):
        print(self.key,end =' ')
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
            
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=' ')
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=' ')


    def delete(self,data,curr):
        if self.key is None:
            print("Tree is empty")
            return 
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,curr)
            else:
                print("given node is not present in the tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data,curr)
            else:
                print("given node is not present in the tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return          
                self = None 
                return temp
            node = self.rchild 
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key,curr)
        return self

    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("node with smallest key is:",current.key)

    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("node with the maximum value is:",current.key)




    
    def find_closest_value(self,target):
        closest = self.key
        min_diff = float('inf')

        current_node = self
        while current_node:
            current_diff = abs(current_node.key - target)

            if current_diff < min_diff:
                min_diff = current_diff
                closest = current_node.key

            if target < current_node.key:
                current_node=current_node.lchild
            elif target > current_node.key:
                current_node = current_node.rchild
            else:
                break

        return closest


def is_valid_bsst(node,left=float('-inf'),right=float('inf')):
    if node is None:
        return True

    if not(left < node.key < right):
        return False

    return (is_valid_bsst(node.lchild,left,node.key) and
            is_valid_bsst(node.rchild,node.key,right))



                
def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)


# root = BST(4)
# list1 = [5,8,5,1,2,9,6]
# for i in list1:
#     root.insert(i)
# print('preorder')
# root.preorder()
# print()
# print('inorder')
# root.inorder()
# print()
# print('postorder')
# root.postorder()

# root.min_node()
# root.max_node()

# print('delelelllele')

# # root.delete(3)
# if count(root) > 1:
#     root.delete(4,root.key)
# else:
#     print("cant perform deletion operation")
# root.inorder()
# print('hjjhjhhjjhh',count(root))








class BSTT:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return 
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BSTT(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BSTT(data)

    

    def search(self,data):
        if self.key == data:
            print("node is found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("node is not present")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("node is not present in this tree")


    def preorder(self):
        print(self.key,end=' ')
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=' ')
        if self.rchild:
            self.rchild.inorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end = ' ')
        if self.rchild:
            self.rchild.inorder()

    
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end= ' ')
        

    

    def delete(self,data,curr):
        if self.key is None:
            print("tree is empty")
            return
        if self.key > data:
            if self.lchild:
                self.lchild = self.lchild.delete(data,curr)
            else:
                print("given node is not present")
        elif self.key < data:
            if self.rchild:
                self.rchild = self.rchild.delete(data,curr)
            else:
                print('given node is not present')

        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key,curr)
        return self
    



    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("node with min key is ",current.key)


    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("node with max value is ",current.key)

    
    def find_closest_value(self,target):
        closest = self.key
        min_diff = float('inf')

        current_node = self
        while current_node:
            current_diff = abs(current_node.key - target)

            if current_diff < min_diff:
                min_diff = current_diff
                closest = current_node.key

            if target < current_node.key:
                current_node=current_node.lchild
            elif target > current_node.key:
                current_node = current_node.rchild
            else:
                break

        return closest


def is_valid_bsst(node,left=float('-inf'),right=float('inf')):
    if node is None:
        return True

    if not(left < node.key < right):
        return False

    return (is_valid_bsst(node.lchild,left,node.key) and
            is_valid_bsst(node.rchild,node.key,right))






def countt(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)




new = BSTT(3)  
list2 = [4,2,5,1,7,6]
for i in list2:
    new.insert(i)
print('preorder')
new.preorder()
print()
print('inorder')
new.inorder()
print()
print('postorder')
new.postorder()
new.max_node()
new.min_node()
if countt(new) > 1:
    new.delete(7,new.key)
else:
    print("cant perform deletion")
print('inorder')
new.inorder()


print('is validdddddd')
print(is_valid_bsst(new))