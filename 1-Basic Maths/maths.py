def countDigits(n:int) -> int:
    """
    You are given a number ’n’.
    Find the number of digits of ‘n’ that evenly divide ‘n’.
    """
    count = 0
    while n > 0:
        last_digit = n % 10
        if last_digit != 0 and n % last_digit == 0:
            count += 1
        n = int(n / 10) #n//=10
    return count
print(countDigits(336))

def reverseNum(n:int) -> int:
    """
    You are given a number ’n’.
    Reverse digits of ‘n’.
    """
    reversed = int()
    while n > 0:
        last_digit = n % 10
        reversed = reversed * 10 + last_digit
        n //= 10
    return reversed
print(reverseNum(1234))

def checkPalindrome(n:int) -> bool:
    i,j = 0,len(str(n)) - 1
    str_n = str(n)
    while i < j:
        if str_n[i] != str_n[j]:
            return False
        i += 1
        j -= 1
    return True
    # return n == str()
print(checkPalindrome(121))

# Better Brute force
def gcd(num1:int,num2:int) -> int:
    min_num = min(num1,num2)
    for i in range(min_num,1,-1): #
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1
print(gcd(20,15))

def euclideanGCD(num1:int,num2:int) -> int:
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    if num1 > num2:
        return euclideanGCD(num1-num2,num2)
    else:
        return euclideanGCD(num1,num2-num1)
print(euclideanGCD(9,12))

# Optimal Euclidean
def gcd_euclidean(num1:int,num2:int) -> int:
    if num2 == 0:
        return num1
    return gcd_euclidean(num2, num1%num2)


def armstrong(num:int) -> bool:
    sum=0
    length=len(str(num))
    original_num = num
    while num > 0:
        last_digit = num % 10
        sum = sum + last_digit ** length
        num //= 10
    if original_num == sum:
        return True
    return False
print(armstrong(153))
print(armstrong(35))

