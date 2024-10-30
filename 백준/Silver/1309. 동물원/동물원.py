import sys

N = int(sys.stdin.readline())
a, b = 1, 1

for _ in range(N):
    a, b = a+2*b, a+b

print(a%9901)
