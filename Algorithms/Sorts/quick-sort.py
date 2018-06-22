def quicksort(array):
    if len(array) <= 1: 
        return array

    return (
        quicksort([x for x in array if x < array[0]])
        + [x for x in array if x == array[0]]
        + quicksort([x for x in array if x > array[0]])
    )

sorted_array = quicksort([9,1,4,6,3,2,8,7,5,0])
print(sorted_array)