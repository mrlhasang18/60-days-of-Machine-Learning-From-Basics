# lets practice on hacker rank:
'''
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for. For each name queried, 
print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found,
print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

'''

# number of key:value pair
n = int(input())
# creating phboook dictionary
phbook = {}

# taking input and storing them into phbook dictionary
for i in range(n):
    name_ph = input().split()
    phbook[name_ph[0]] = name_ph[1]
    
while True:
    try:
        inp = input()
        if inp in phbook:
            print(inp+"="+phbook[inp])
        else:
            print("Not found")
    except EOFError:
        break
    