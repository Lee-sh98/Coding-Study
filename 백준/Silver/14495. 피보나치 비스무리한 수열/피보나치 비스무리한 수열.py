import sys

n = int(sys.stdin.readline())
a = b = c = 1
for i in range(n-3):
    a, b, c = b, c, a+c

print(c)
