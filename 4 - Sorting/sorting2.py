def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_side = merge_sort(arr[:mid])
    right_side = merge_sort(arr[mid:])
    return merge(left_side, right_side)

def merge(left_side,right_side):
    l,r = 0,0
    len_l,len_r = len(left_side), len(right_side)
    temp = []
    while l < len_l and r < len_r:
        if left_side[l] <= right_side[r]:
            temp.append(left_side[l])
            l += 1
        else:
            temp.append(right_side[r])
            r += 1
    while l < len_l:
        temp.append(left_side[l])
        l += 1
    while r < len_r:
        temp.append(right_side[r])
        r += 1
    
    return temp

arr = [38, 27, 43, 3, 9, 82, 10]
arr = merge_sort(arr)
print(arr)

