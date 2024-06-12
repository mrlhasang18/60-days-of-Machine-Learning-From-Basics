'''
deleting a node: 
1. the leaf node: which doesn't have any child nodes
2. Deleting a node with 1 child
3. Deleting a node with 2 child
'''

# node creation

class bst:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = bst(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = bst(data)
                
    def search(self,val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    # highest element
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    # lowest element
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    # node deletion
    def delete(self,val):
        # lefts of tree
        if val < self.data:
            if self.left:
                # if there is a left subtree
                self.left = self.left.delete(val)
        
        # rights of tree
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
                
        else:
            # at the leaf node: no child
            if self.left is None and self.right is None:
                return None
            # has right child node
            if self.left is None:
                return self.right
            # has left child node
            if self.right is None:
                return self.left
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self
    
    def inorder_traversal(self):
        element= []
        
        # left node
        if self.left:
            element += self.left.inorder_traversal()
        
        # base node
        element.append(self.data)
        
        # right node
        if self.right:
            element += self.right.inorder_traversal()
            
        return element


def buildTree(elements):
    root = bst(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34]
    numbers_tree = buildTree(numbers)
    print("Before deleting: ",numbers_tree.inorder_traversal())
    print(numbers_tree.search(20))
    print(numbers_tree.search(21))
    
    numbers_tree.delete(20)
    print("After deleting: ",numbers_tree.inorder_traversal())