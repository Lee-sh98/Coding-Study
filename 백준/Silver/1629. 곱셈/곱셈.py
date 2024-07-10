import sys

def power(a, b, c):
    res = 1
    while b:
        if b&1:
            res*=a
        a*=a
        a = a%c
        b>>=1
    return res%c

A, B, C = map(int, sys.stdin.readline().split())

print(power(A, B, C))
