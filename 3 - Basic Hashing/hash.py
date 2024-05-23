def findNum(n,arr):
    count = 0
    for i in range(len(arr)):
        if n == arr[i]:
            count += 1
    return count
#print(findNum(1,[1,2,3,4,5,1,2,1]))
## Extremely high computation time

## To solve this hashing is used.
def hashArray(arr):
    hash_array=[0] * (max(arr) + 1) #max instead of len to ensure IndexError doesnot occur if any value of arr is more than len(arr)
    for i in range(len(arr)):
        hash_array[arr[i]] += 1

    for i in range(len(hash_array)):
        print(f"{i} -> {hash_array[i]}")
#print(hashArray([1,2,3,4,5,10,12,1]))


def stringHash(s):
    string_hash = [0] * 26
    for i in range(len(s)):
        string_hash[ord(s[i]) - ord('a')] += 1
    for i in range(len(string_hash)):
        print(f"{chr((i+ord('a')))} -> {string_hash[i]}")
#print(stringHash("hello"))

#def highest_lowest_brute(arr):



# Optimal way to find highest and lowest freq items using hashmap/dictionary
def highest_lowest(arr):
    freq={}
    for i in range(len(arr)):
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1
    min_freq = list(freq.values())[0]
    max_freq = list(freq.values())[0]
    for val in freq.values():
        if min_freq > val:
            min_freq = val
        if max_freq < val:
            max_freq = val
    return min_freq,max_freq
    # min_element =[]
    # max_element = []
    # for key,val in freq.items():
    #     if val == min_freq:
    #         min_element.append(key)
    #     if val == max_freq:
    #         max_element.append(key)
    # return min_freq,min_element, max_freq, max_element
print(highest_lowest([10,10,20,20,30,30,40,40,50,50,10,100]))