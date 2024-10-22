import sys

a, b, c = sorted(map(int, sys.stdin.readline().split()))

print(a+b+(a+b-1 if a+b <= c else c))
