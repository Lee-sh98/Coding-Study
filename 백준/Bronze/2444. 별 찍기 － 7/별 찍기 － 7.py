# make a star

import sys
input = sys.stdin.readline

N = int(input())

for x in range(-N+1,N):
    print(" " * abs(x) + "*"*(2*(N-abs(x))-1))
