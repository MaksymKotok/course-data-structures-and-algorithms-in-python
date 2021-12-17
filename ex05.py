def fib(num):
    return fib(num - 1) + fib(num - 2) if num > 1 else 1 if num == 1 else 0
