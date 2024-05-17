def printToN(i,n):
    if i > n:
        return
    print(i)
    printToN(i+1,n)
#printToN(1,10)

def printStringNTimes(count,name,n):
    if count > n:
        return
    print(name)
    printStringNTimes(count+1,name,n)
#printStringNTimes(1,"Hello",5)

def printNTo1(i,num):
    if i < 1:
        return
    print(i)
    printNTo1(i-1,num)
#printNTo1(10,10)

# Parameterized
def sumOfSeries(i,n,total=0):
    if i > n:
        print(total)
        return
    sumOfSeries(i+1,n,total+i)
#sumOfSeries(1,3)

# Function-based
def sumOfSeries1(n):
    if n == 0:
        return 0
    return n + sumOfSeries1(n-1)
#print(sumOfSeries1(3))

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
#print(factorial(5))
    
#Extra parameter for position from which swap should occur, ideally 0th position
def swap(i,n):
    if i >= len(n)//2:
        return
    n[i],n[len(n)-i-1] = n[len(n)-i-1],n[i]
    swap(i+1,n)
    return n
#print(swap(0,[1,2,3,4,5,6,7]))

# Two pointer recursive swap.
def swapArray(l,r,n):
    while l >= r:
        return
    n[l],n[r] = n[r],n[l]
    swapArray(l+1,r-1,n)
    return n
#print(swapArray(0,len([1,2,3,4,5])-1, [1,2,3,4,5]))

def palindrome(i,s):
    if i >= len(s)//2:
        return True
    if s[i] != s[len(s)-i-1]:
        return False
    return palindrome(i+1,s)
print(palindrome(0,"abba"))


