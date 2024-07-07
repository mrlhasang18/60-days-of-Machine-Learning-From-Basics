# Day 32/60 of learning Machine Learning from basics
# Lambda function:
# Lambda function is actually fairly simple as it's just a one line anonymous function.
# It can accept any number of parameters and they can return any valid python expression.

# demo: single parameter lambda function

add = lambda x:x+1
'''
This above is same as the 
def add(x):
    return x+1
'''

# calling funciton
res = add(2)
print(res)

# demo: double parameter lambda function

add = lambda x,y:x+y

# calling funciton
res = add(2,3)
print(res)


#