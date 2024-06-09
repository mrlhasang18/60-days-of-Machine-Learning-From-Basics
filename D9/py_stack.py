# Now let's use python's built in stack (i.e. LifoQueue)
# It has put as push and get as pop operaiton

# Importing queue module for LifoQueue that is same as stack in pyhton
import queue as q

student = q.LifoQueue(maxsize=3)

# Printing the size of stack
print("The size of stack is: ",student.qsize())

# Push operation
student.put(input("push: "))

# Printing the size of stack
print("The size of stack is: ",student.qsize())

# Pop operation
print("Popped: ",student.get())
print("The size of stack is: ",student.qsize())

# Checking whether stack is empty or not using empty() method
print("Stack is empty: ",student.empty())