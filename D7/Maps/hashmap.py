# [Note: For theory go to the 1.Theory.txt file ]

# Practical implementation of Dictionary (i.e hashmap in python)
from collections import defaultdict

# Dictionary creation:

dict = {
    'name': 'lhasang',
    'age': 19,
}

# Accessing the dictionary:
print(type(dict))
print(dict)

# Accessing the value of the key:

print(dict['name'])

# replacing the value of key

dict['name'] = 'lhasang sherpa'
print(dict['name'])

# Adding new key:value 

dict["sex"] = "male"
print(dict)

# Revoving elements
del dict['sex']
print(dict)

# Searching keys using get method
print(dict.get("sex"))
print(dict.get("name"))

# Retrieve all the key:value pairs in tuple format
print(dict.items())

# let's iterate over key value pairs
for key, value in dict.items():
    print(" your {} is {}".format(key,value))
    
# captitalize the keys
print(" --------- Keys in capital ------")
for key in dict.keys():
    print(key.upper())

# let's create a default answer when unstored key is searched
dict = defaultdict(lambda: "The key doesn't exist !!")
print(dict['lama'])

# Deleting all the key:value pair
dict.clear()
print(dict)
