def selection_sort(arr):
    """
    Set i to minimum in outer loop,
    Start inner loop with i+1 to len(arr)
    if arr[inner_loop] < arr[minimum at i] change minimun to inner loops index
    swap arr[min],arr[i]
    """
    for i in range(len(arr)-1):
        minimum_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minimum_index]:
                minimum_index = j
        arr[minimum_index],arr[i] = arr[i],arr[minimum_index]
    return arr
#print(selection_sort([4,1,2,3,5,10,6,7]))

def selection_sort_reverse(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i+1,len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[max_index],arr[i] = arr[i],arr[max_index]
    return arr
#print(selection_sort_reverse([4,1,2,3,5,10,6,7]))

def bubble_sort(arr):
    for i in range(len(arr)):
        flag = 0
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag += 1
        if flag == 0:
            break
    return arr
    
print(bubble_sort([4,1,2,3,5,10,6,7]))
