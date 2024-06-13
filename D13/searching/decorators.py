'''
decorators in python are designed to add the extra functionality to the methods or functions without directly 
modifying their source code.
Decorators act as a wrapper for yout original function.
Common uses of decorators are:
1)Logging
2)Timing

How to apply decorators:
just write it before the function that you want to modify
'''

import time

def time_it(func):
    def wrapper(*args, **kwargs):
        #records start time
        start = time.time()
        result = func(*args,**kwargs)
        #records end time
        end = time.time()
        print(func.__name__ +" took "+ str((end-start)*1000)+ " mil-sec")
        return result
    return wrapper


# lets create a function that sums

@time_it
def sum(num):
    result = []
    for n in num:
        result.append(n+n)
    return result


@time_it
def mul(number):
    result = []
    for num in number:
        result.append(num * num)
    return result

numbers = [1, 2, 3, 4, 5]

result_sum = sum(numbers)

result_mul = mul(numbers)
