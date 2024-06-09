'''
In python we have LifoQueue : pythons queue module
                            : which behaves as a stack. 
Stack is an linear Data structure that follows Last In First Out principle( i.e. lIFO)
It has two main operations push and pop. 
push is used to insert element in stack and pop is used to remove the element from stack. 
It has other operations like peek, isempty, isfull etc. 

'''
import queue
# Node creation

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
# Stack creation

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        
# push operation

    def push(self,data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        else:
            self.top  = new_node
            
# pop operation
    def pop(self,data):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

# peek operation

    def peek(self) -> list:
        if self.top:
            return self.top.data
        else:
            return None
        
        
# data insertion

a = Stack()
print(" ------ Stack implementation using singly linked list ------")
a.push(int(input("Push : ")))
print(a.peek())
a.pop(int(input("Pop : ")))
print(a.peek())


# Output: 3