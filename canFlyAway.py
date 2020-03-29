# h < arr[i] => false
# arr[i] - arr[i-1] > 1000 => false

def canFlyAway(h,arr):
    for _ in arr:
        if h > _:
            return False
            break
    for _ in range(len(arr)-1):
        if abs(arr[_] - arr[_+1]) > 1000:
            return False
            break
    return True
