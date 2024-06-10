# In python we have modules for queue:
# 1. Queue
# 2. LifoQueue: But it acts as stack

# We can also deque from the collections

from collections import deque

food = deque()   #instance of deque

# Enqueue in queue

food.appendleft("Mo:Mo")   # Insert from the tail
food.appendleft("Chowmin")
food.appendleft("Chicked DrumStick")

# Dequeue in queue: remove from the head
print("------ Elements in queue ------")
print(food)

print("Deque operation in queue: \n")
print("Dequeued element: ",food.pop())
print("Dequeued element: ",food.pop())
print("Dequeued element: ",food.pop())
print("\nQueue is empty: ",food)