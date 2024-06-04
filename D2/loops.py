'''
loops and iterables: Iterable is something that you can loop over
'''

# for loop: 
a =[4,5,3,6]

for i in range(len(a)):
    if a[i]%2==0:
        print(a[i])
        
#while loop
print("\n")
i=0
while i<len(a):
    print(a[i])
    i+=1


#lets create a custom for looop
def custom_for_loop(iterable, action_to_do):
    iterator = iter(iterable)
    done_looping = False
    while not done_looping:
        try:
            item = next(iterator)
        except StopIteration:
            done_looping = True
        else:
            action_to_do(item)
            
numbers = {1, 2, 3, 4, 5}
custom_for_loop(numbers, print)

#Let's create simple calculator 

print("\n-------- simple calculator -------\n Operations: \n1.+   2.- \n3.*   4./ \n")
a =int(input("Enter first number: "))
b=int(input("Enter second number: "))

op = str(input("Enter operation: "))
ch = int(input("\nEnter 1 for calculation and 2 for exit\n"))
def calc(a,b,op):
    return{
        '+': a+b,
        '-': a-b,
        '*': a*b,
        '/': a/b
    }[op]

print(calc(a,b,op))

