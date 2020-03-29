def sumOfOddNumber(a,b):
    sumOdd = 0
    for _ in range(a,b+1):
        if _ %2 !=0:
            sumOdd+=_
    return sumOdd