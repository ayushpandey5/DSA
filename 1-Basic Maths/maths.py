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
