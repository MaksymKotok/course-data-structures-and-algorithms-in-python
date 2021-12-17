def factorial(num):
    return num * factorial(num - 1) if num > 0 else 1
