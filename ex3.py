def productOfArray(arr):
    prod = 1
    for i in range(len(arr)):
        prod *= arr[i]
    return prod