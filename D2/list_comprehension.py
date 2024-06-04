'''
List comprehension : provides shorter syntax uses for loop inside list
syntax:
newlist = [expression for item in iterable if condition == True]

'''
# Example 1
# Create a list of squares of numbers from 0 to 9
squares = [i**2 for i in range(10)]
print(squares)

#Example 2
city = ["bhaktapur", "kathmandu", "lalitpur", "Surkhet"]

# Create a list containing only the items that are city
newlist = [x for x in city if "a" in x]
print(newlist)  

#list inside list

a = [[i**2 for i in range(4)] for j in range(5)]
print(a)