# Quick sort: This technique uses divide and conquer approach to divide given list into partitions and 
# then recursively sort these partitions. 
# It starts with a pivot element and tries to put pivot element in its correct position.
# There are two types of partitions :
# 1. Lomuto partition 2. Hoare partition

# It's avg time complexity is O(nlogn) and worst time complexity is O(n^2)


# let's implement it in a code:
def quick_sort(elements):
    if len(elements) == 1:
        return elements
    
    if len(elements) == 0:        # This is the quick sort using recursion.
        return []
    
    pivot = elements[-1]
    smaller = []
    greater = []
    
    for i in range(len(elements)-1):
        if elements[i] < pivot:
            smaller.append(elements[i])
        else:
            greater.append(elements[i])
            
    return quick_sort(smaller) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    print("\n----------- Quick sort -----------\n")
    elements = [5,99,2,1,10,34,88,34]
    print("Before sorting: ",elements)
    elements = quick_sort(elements)
    print("After sorting : ",elements)