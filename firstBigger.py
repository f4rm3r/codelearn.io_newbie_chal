def firstBigger(a,b):
    if b%a ==0:
        return a+b
    else:
        return a+b-(b%a)
