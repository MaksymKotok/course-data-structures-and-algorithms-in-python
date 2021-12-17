def recursiveRange(num):
    return num + recursiveRange(num - 1) if num > 0 else 0
