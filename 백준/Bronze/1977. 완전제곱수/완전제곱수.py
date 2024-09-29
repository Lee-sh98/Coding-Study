import sys
from math import ceil
input = sys.stdin.readline

M, N = int(input()), int(input())
s = 0
m = 0
for num in map(int(2).__rpow__, range(1, 101)):
    if M<=num<=N:
        if s==0:
            m = num
        s += num

if s == 0:
    print(-1)
else:
    print(s)
    print(m)
