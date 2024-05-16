def printToN(i,n):
    if i > n:
        return
    print(i)
    printToN(i+1,n)
printToN(1,10)

def printStringNTimes(count,name,n):
    if count > n:
        return
    print(name)
    printStringNTimes(count+1,name,n)
printStringNTimes(1,"Hello",5)
