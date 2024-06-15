# Insertion sort: Insertion sort is a simple sorting algorithm (Very few lines of code) that is best for small lists.
# It uses one part of the array to hold the sorted values,
# and the other part of the array to hold values that are not sorted yet.


# Implementation

def insertion_sort(elements):
    
    for i in range(1,len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor
        
if __name__ == '__main__':
    print("\n----------- Insertion sort -----------\n")
    elements = [2,99,112,1,10,34,88,34]
    print("Before sorting: ",elements)
    insertion_sort(elements)
    print("After sorting : ",elements)