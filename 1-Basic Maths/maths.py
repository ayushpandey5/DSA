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



