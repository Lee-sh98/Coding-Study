import sys

def gcd(a, b):
    return abs(a*b)//lcd(a, b)

def lcd(a, b):
    c, d = a, b
    while c!=d:
        if c>d:
            d += b
        else:
            c += a
    return c

A, B = map(int, sys.stdin.readline().split())
print(gcd(A, B))
print(lcd(A, B))
