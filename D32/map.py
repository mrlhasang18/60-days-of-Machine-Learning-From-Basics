# Applting lambda in maps

num = [1,2,3,4,5,6,7,8,9,10]

'''
def square(x):
    return x**2

# using map function

squares = list(map(square, num))
print(squares)

'''

# using lambda function

squares = list(map(lambda x:x**2, num))
print("Square: ",squares)

# Filter functions
# Apply function to every sungle value inside of list/iterable object

even = list(filter(lambda x:x%2==0,num))
print("Even numbers: ",even)

# some sort of sorting

val = [(1,"b","lama"),(2,"a","apple"),(3,"c","omg")]

sorted_val = sorted(val, key=lambda x: x[1])

print(list(sorted_val))