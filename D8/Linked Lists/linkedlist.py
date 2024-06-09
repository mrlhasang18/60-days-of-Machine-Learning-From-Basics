
# [note: For theory checkout the 1.Theory.txt file in the same folder of the repository]

'''
Linked list methods: 
- insert_at_beginning()
- insert_at_end()
- remove_at_beginning()
- remove_at_end()
- insert_at()
- remove_at()
- search()
'''
# Linked list creaion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    

    #lets implement the methods
    # insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
    #check if linked list is empty
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        
    # insert at the end

    def insert_at_end(self,data):
        new_node = Node(data)
    #check if linked list is empty
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node 
        
    # search
    def search(self,data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else: 
                current_node = current_node.next


# Now lets remove from the linked list
# remove from the beginning
    def remove_at_beginning(self):
        if self.head:
            self.head = self.head.next
        else:
            print("Linked list is empty")
        

# remove from the end
    def remove_at_end(self):
        if self.head:
            current_node = self.head
            while current_node:
                if current_node.next == self.tail:
                    current_node.next = None
                    self.tail = current_node
                else:
                    current_node = current_node.next
        else:
            print("Linked list is empty")
            
#lets insert and remove data from the linked list
student = LinkedList()
student.insert_at_end("first")
student.insert_at_end("last")
student.insert_at_beginning("Top")
print(LinkedList)
print(student.search("last"))
print(student.search("hello"))
student.remove_at_end()
print(student.search("last"))