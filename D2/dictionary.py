#DAY 2 OF LEARNING ML FROM BASICS 

#Dictionary->Collection of items/data with key:value pair

dict = {
    "name":"Lhasang",
    "age":18,
    "city":"Kathmandu"
}
print(type(dict))
print("name" in dict)

#Dictionary items
print(dict.items())
print(dict["name"])

print(len(dict))  #outputs 3 due to 3 key:value pair in dict

#In dictionary no duplications are allowed, if then new will overrite the old key:value

dict["name"] = "Lama"  #adding items 
print("Name changed to: ",dict["name"])

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
europe['data'] = {'capital':'rome','population':59.83}

# Add sub-dictionary for 'italy' to europe
europe['italy'] = {'capital': 'rome', 'population': 59.83}
del(europe['data'])

# Print europe
print(europe)
