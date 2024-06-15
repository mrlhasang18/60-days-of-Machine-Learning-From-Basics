# Bubble sort is a sorting technique used to sort a list or an array.
# It performs sorting in O(n^2) time complexity  and space complexity O(1) so it is not the most efficient.
# It compares the two and then repeat and sorts the list or an array.


# Implementation

def bubble_sort(elements):
    
    size = len(elements)
    
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    print("\n----------- Bubble sort -----------\n")
    elements = [5,99,2,1,100,34,88,34]
    print("Before sorting: ",elements)
    bubble_sort(elements)
    print("After sorting : ",elements)


