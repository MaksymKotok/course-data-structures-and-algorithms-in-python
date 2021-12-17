def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
        
def someRecursive(arr, f):
    return True if f(arr[0]) is True else someRecursive(arr[1:], f) if len(arr) > 1 else False
