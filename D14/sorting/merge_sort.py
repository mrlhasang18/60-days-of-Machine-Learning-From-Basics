# Merge sort is a sorting algorithm that gives time complexity of O(nlogn) and thus performs better
# than insertion sort, bubble sort etc.

# Implementation:

def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge_two_sorted_lists(left, right, arr)


# lets merge these 2 sorted arrays
def merge_two_sorted_lists(a,b,arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1
    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1
    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1

if __name__ == '__main__':
    print("\n----------- Merge sort -----------\n")
    lists = [
        [45, 2, 15, 7, 8, 23, 58, 29],
        [],
        [3,5,6],
        [9,8,7,2],
        [1,2,3,4,5]
    ]
    
    # for all the arrays/lists in the lists
    for arr in lists:
        merge_sort(arr)
        print(arr)