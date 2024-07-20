import sys
input = sys.stdin.readline

def get_gcd(a, b):
    while a%b:
        a, b = b, a%b
    return b


p, q = map(int, input().split())
r, s = map(int, input().split())

a, b = p*s+r*q, q*s

gcd = get_gcd(a, b)

print(a//gcd, b//gcd)
