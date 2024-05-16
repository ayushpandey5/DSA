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

def sumOfSeries(i,n,total=0):
    if i > n:
        print(total)
        return
    sumOfSeries(i+1,n,total+i)
#sumOfSeries(1,3)