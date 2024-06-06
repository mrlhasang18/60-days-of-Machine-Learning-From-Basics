# You have to take resposnibilty for the errors that may occur in your program

# Example:

# a = int(input("Enter a number: "))
# print(a+3)

# It's ok if user just inputs the number but what if they input strings: that will be an value error
# To handle this we developers must know Exception handling :
# we use try and except block

try:
    a = int(input("Enter a number: "))
    print(a+3)
    
except Exception as e:
    print("Error occured: ",e)