def stabilityArray(arr):
    for _ in range(len(arr)-1):
        if abs(arr[_] - arr[_+1]) >5:
            return False
            break
    return True
