def allOdd(n):
    n = str(n)
    oddNumber = "2,4,6,8,0"
    for _ in n:
        if _ not in oddNumber:
            return False
            break
    else: return True
print (allOdd(input("n> ")))