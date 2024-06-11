# Binary search tree implementation

#  Node creation
class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self,data):
        if data == self.data:
            return
        #adding in left
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
                
        # adding in  right
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)
                
    # In order traversal
    def in_order_traversal(self):
        elements = []
        
        # visit the left node
        if self.left:
            elements += self.left.in_order_traversal()
            
        # visit base node
        elements.append(self.data)
        
        #visit the right node
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
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
            
def build_tree(elements):
    root = BST(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    fruit = ["banana","pineapple","mango","apple","guava"]
    a = build_tree(fruit)
    print(a.in_order_traversal())
    
    # searching in tree
    print(a.search("mango"))
    a.add_child("mango")
    # Binary tree doesn't allow multiple same value like in a set
    print(a.in_order_traversal())
    print(a.search("aalu"))