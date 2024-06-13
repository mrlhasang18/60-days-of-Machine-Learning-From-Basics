'''
* Searching and sorting are one of the most important algorithm and problems that we face and solve in computer.
  Although there are several searching algorithms but we have to use the one that has less time complexity and
  is faster.Binary search is a searching algorithm that finds the position of a target value within a sorted array.
  In binary search, Iteration k = n/2^k
  Time complexity, linear search : O(n)
                   Binary search : log(n)
'''
from decorators import time_it

@time_it
def linear_search(list, numbertofind):
    for index, element in enumerate(list):
        if element == numbertofind:
            return index
    return -1
    
@time_it
def binary_search(list, numbertofind):
    left_index = 0
    right_index = len(list)-1
    middle_index = 0
    
    while left_index <= right_index:
        middle_index = (left_index+right_index)//2   # // is because / returns floating point but index is int
    
        # mid number
        mid_number = list[middle_index]
        if mid_number == numbertofind:
            return middle_index
        
        if mid_number < numbertofind:
            left_index = middle_index +1
            
        elif mid_number > numbertofind:
            right_index = middle_index -1
    return -1


if __name__ == '__main__':
    #num = [2,1,56,34,87,23]
    #to_find = 87
    
    # lets go with big numbers
    num = [i for i in range(10001111)]
    to_find = 1000001
    
    index = linear_search(num, to_find)
    print("\n----------- Linear search O(n) ------------\n")
    print(f"{to_find} number is at index : ", index)
    
    print("\n----------- Binary search O(logn) ------------\n")
    print(f"Binary search:\n{to_find} number is at index : ", binary_search(num, to_find))