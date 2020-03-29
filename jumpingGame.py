def jumpingGame(arr,h,t):
    if h >= arr[0]:
        tmp = 0 
        for _ in arr:
            if h + tmp < _:
                return False
                break
            tmp += t
        return True
    else: return False