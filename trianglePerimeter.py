def trianglePerimeter(a, b, c):
    check = abs(b-c) < a < b + c
    if check == True:
        return a+b+c
    else: return False
