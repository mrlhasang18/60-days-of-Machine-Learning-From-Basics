'''
decorators in python are designed to add the extra functionality to the methods or functions without directly 
modifying their source code

How to apply decorators:
just write it before the function that you want to modify
'''

import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took "+ str(end-start)*1000+ " mil sec")
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


# Recursion for binary search

def binary_search(num_list, num_to_find, left_index, right_index):
    if right_index < left_index:
        return -1
    
    middle_index = (left_index + right_index) // 2
    
    if middle_index >= len(num_list) or middle_index < 0:
        return -1
    
    mid_num = num_list[middle_index]
    
    if mid_num == num_to_find:
        return middle_index
        
    if mid_num < num_to_find:
        return binary_search(num_list, num_to_find, middle_index + 1, right_index)
    else:
        return binary_search(num_list, num_to_find, left_index, middle_index - 1)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    result_sum = sum(numbers)
    print(result_sum)  # [2, 4, 6, 8, 10]

    result_mul = mul(numbers)
    print(result_mul)  # [1, 4, 9, 16, 25]

    num = [1, 2, 23, 34, 56, 87]  # sorted list
    to_find = 23
    print("\n----------- Binary search O(logn) ------------\n")
    print(f"Binary search:\n{to_find} number is at index : ", binary_search(num, to_find, 0, len(num) - 1))