import sys

K = int(sys.stdin.readline())
a, b = 0, 1

for _ in range(K-1):
    a, b = b, a+b

print(a, b)
