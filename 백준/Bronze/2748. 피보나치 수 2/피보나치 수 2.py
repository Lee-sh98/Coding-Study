import sys

def fib(n):
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    yield b

n = int(sys.stdin.readline())

print(*fib(n))
