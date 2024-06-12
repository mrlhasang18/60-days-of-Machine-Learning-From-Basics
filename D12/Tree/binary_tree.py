# In this exercise I am doing the following :
# - pre and post order traversal in a Binary Search Tree
# - Find minimun and maximum element in a Binary Tree


# node creation

class BST:
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
                self.left = BST(data)
                
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)
                
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements
        
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    
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

if __name__ == "__main__":
    name = ["lhasang","Rakesh","Aayush","Safal","Hari"]
    name_tree = build_tree(name)
    print(name_tree.search("lhasang"))
    name_tree.add_child("lakpa")
    # inorder traversal
    print(" --------- Inorder traversal ---------")
    print(name_tree.inorder_traversal())
    # post-order traversal
    print(" --------- Post traversal ---------")
    print(name_tree.post_order_traversal())
    # pre-order traversal
    print(" --------- Pree traversal ---------")
    print(name_tree.pre_order_traversal())
    # Largest element
    print(" --------- Largest element ---------")
    print(name_tree.find_max())
    # Smallest element
    print(" --------- Smallest element ---------")
    print(name_tree.find_min())