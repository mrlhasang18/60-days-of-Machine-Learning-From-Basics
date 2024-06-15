'''
selection sort: simple sorting algorithm that works by repeatedly selecting the smallest 
(or largest, depending on the ordering) element from the unsorted portion of the list and moving 
it to the beginning (or end) of the sorted portion of the list.

Selection sort is a simple algorithm for sorting, it gives o(n^2) BIG O complexity.

'''

# Code Implementation
def selection_sort(elements):
    
    size = len(elements)
    
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1, size):
            if elements[j] < elements[min_index]:
                min_index = j
        if i != min_index:
            elements[i], elements[min_index] = elements[min_index], elements[i]



if __name__ == '__main__':
    print("\n----------- Selection_sort -----------\n")
    lists = [
        [45, 2, 15, 7, 8, 23, 58, 29],
        [],
        [3,5,6],
        [9,8,7,2],
        [1,2,3,4,5]
    ]
    
    # for all the arrays/lists in the lists
    for arr in lists:
        selection_sort(arr)
        print(arr)