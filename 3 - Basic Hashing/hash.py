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
print(stringHash("hello"))