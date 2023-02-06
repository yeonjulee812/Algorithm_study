N = int(input())

def Fibonacci(n):
    if n >= 2:
        return Fibonacci(n-2) + Fibonacci(n-1)
    elif n == 0:
        return 0
    elif n == 1:
        return 1

print(Fibonacci(N))
