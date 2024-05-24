def selection_sort(arr):
    for i in range(len(arr)-1):
        minimum_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minimum_index]:
                minimum_index = j
        arr[minimum_index],arr[i] = arr[i],arr[minimum_index]
    return arr

print(selection_sort([4,1,2,3,5,10,6,7]))

