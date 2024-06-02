## Without low mid high params
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[0:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left_half, right_half):
    l,r = 0,0
    temp = []

    while l < len(left_half) and r < len(right_half):
        if left_half[l] <= right_half[r]:
            temp.append(left_half[l])
            l += 1
        else:
            temp.append(right_half[r])
            r += 1

    while l < len(left_half):
        temp.append(left_half[l])
        l += 1
    
    while r < len(right_half):
        temp.append(right_half[r])
        r += 1

    return temp
#print(merge_sort([5,4,3,2,1]))
