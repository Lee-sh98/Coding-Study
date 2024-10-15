import sys

def diff(x, y):
    return x//y + (x%y != 0)

A, B = map(int, sys.stdin.readline().split())
a, b = A, B
while a != b:

    if a > b:
        b += diff(a-b, B)*B
    else:
        a += diff(b-a, A)*A

print(a)
