# Queue is a linear data structure that follows FIFO (First In First Out) princtiple
# It can be implemented using the singly linked list
# Queue has two parts head and tail: we can only insert from tail and that method is called Enqueue.
# We can only remove from head and that method is called Dequeue

# Node Creation

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        
# Queue Creation

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def is_empty(self):
        return self.head is None
    
    # Storing from the tail: Enqueue Operation
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    # Removing from the head: Dequeue Operation
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot Dequeue")
            
        temp = self.head
        self.head = temp.next
        if self.head is None:
            self.tail = None
        return temp.data
    
    def __str__(self):
        result = []
        temp = self.head
        while temp:
            result.append(str(temp.data))
            temp = temp.next
        return "[" + ", ".join(result) + "]"
    
a = Queue()
a.enqueue("ram")
print(a)
a.enqueue(18)
print(a)
print("Dequeued element: ",a.dequeue())
print(a)