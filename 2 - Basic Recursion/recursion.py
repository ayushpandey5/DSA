def printToN(i,n):
    if i > n:
        return
    print(i)
    printToN(i+1,n)

printToN(1,10)