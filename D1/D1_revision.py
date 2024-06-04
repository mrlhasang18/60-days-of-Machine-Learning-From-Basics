#Day 1 
print("Day 1 : Revision of python")

#variables

a=10
b=5

#swapping variables

print("Before swapping: a=",a," b=",b)
temp = a
a=b
b=temp
print("After swapping: a=",a," b=",b)

#operations on variables

print("Addition of a and b is",a+b)

#defining function
def add(a,b):
    print("Addition of c and d is",a+b)


#function call
add(5,6)

#taking input from user
a = input("\nEnter your name: ")
print("Hi ",a,"!")

#even or odd number using function

def EorO(n):
    return print("odd") if(n%2==1) else print("even")
        
EorO(int(input("Enter a number: ")))

#lists

a=[4,6,3,2,8,10.5,"hello"]
print(type(a))
print(a)
#print(sorted(a,reverse=False))   shows type error since sorting needs same datatype value int

#indexing
print(a[0])

#slicing
print(a[1:3])
print(a[-1])

#list methods

a.append(5)
print(a)
a.remove("hello")
a.remove(10.5)
print(a)
print("Sorted list: ",sorted(a,reverse=False))

print(a.index(2))

#in operator in list

print(10 in a)

#tuples:  same as list but
#1. immutable : no item assignment
#2. faster than list
#3. used for fixed data
#4. uses paranthesis insted of brackets

b = (1,6,3)
print(b)
#b[1] = 2 

a=10
b=5

#swapping variables

print("Before swapping: a=",a," b=",b)
a,b=b,a
print("After swapping: a=",a," b=",b)

