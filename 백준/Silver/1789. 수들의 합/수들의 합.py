import sys

S = int(sys.stdin.readline())
n = 1
target = (-1+(1+8*(S+1))**0.5)/2
while n<target:
    n += 1

print(n-1)
