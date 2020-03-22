def ducksHunting(h, arr):
    total = 0
    for _ in arr:
        if _ <= h:
            total +=1
    return total