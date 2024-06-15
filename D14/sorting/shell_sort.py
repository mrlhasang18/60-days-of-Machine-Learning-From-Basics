# Shell sort is a customization over insertion sort. 
# Insertion sort requires many swaps and comparisons if heavy elements are located towards the end of an array. 
# Shell sort will initially sort subarrays that are equal distance apart.

def shell_sort(elements):
    size = len(elements)
    gap = size//2

    while gap > 0:
        for i in range(gap,size):
            anchor = elements[i]
            j = i
            while j >= gap and elements[j-gap] > anchor:
                elements[j] = elements[j-gap]
                j -= gap
            elements[j] = anchor
        gap = gap//2
        

if __name__ == '__main__':
    print("\n----------- Shell sort -----------\n")
    lists = [
        [45, 2, 15, 7, 8, 23, 58, 29],
        [],
        [3,5,6],
        [9,8,7,2],
        [1,2,3,4,5]
    ]
    
    # for all the arrays/lists in the lists
    for arr in lists:
        shell_sort(arr)
        print(arr)