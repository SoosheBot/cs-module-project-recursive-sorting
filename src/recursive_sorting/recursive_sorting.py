# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # To-do
    # Loop through the merged array
    # If the arrays are bigger than zero, find out which element is bigger
    # pop(?) that smaller element into the merged_arr
    for i in range(len(merged_arr)):
        if len(arrA) > 0 and len(arrB) > 0:
            #if arrA at the 0th position is bigger than arrB at the 0th position, pop out the element in arrB's 0th position
            if arrA[0] > arrB[0]:
                merged_arr[i] = arrB.pop(0)
            else:
                #pop the element in arrA's 0th position
                merged_arr[i] = arrA.pop(0)
        else:
            # if arrA is empty, add rest of arrB to merged array
            if len(arrA) == 0:
                merged_arr[i] = arrB.pop(0)
            else:
                merged_arr[i] = arrA.pop(0)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",arr)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    #literally only named it this so I'd know what it is
    other_half_of_array_start = mid + 1

    #if array is already sorted
    if arr[mid] <= arr[other_half_of_array_start]:
        return

    while start <= mid and other_half_of_array_start <= end:

        if arr[start] <= arr[other_half_of_array_start]:
            start += 1
        else:
            value = arr[other_half_of_array_start]
            index = other_half_of_array_start

            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            
            arr[start] = value

            start += 1 
            mid += 1
            other_half_of_array_start += 1

    return arr


# def merge_sort_in_place(arr, l, r):
#     # Your code here


#     return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
