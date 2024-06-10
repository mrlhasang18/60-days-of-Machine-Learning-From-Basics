# Queue can also be implemented using list

walmart_stock = []

# Enqueue : Adding from the tail
walmart_stock.insert(0,10000010)
walmart_stock.insert(0,1000005)
walmart_stock.insert(0,1000000)

print("Queue implementation using List:",walmart_stock)

# Dequeue : removing from the head

print("Dequeued element : ",walmart_stock.pop())
print("Dequeued element : ",walmart_stock.pop())
print("Dequeued element : ",walmart_stock.pop())


# So list follows the FIFO rule for the queue implementation