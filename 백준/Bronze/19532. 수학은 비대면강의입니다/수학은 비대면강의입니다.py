import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

x = (c*e-b*f)//(a*e-b*d)
y = (a*f-c*d)//(a*e-b*d)

print(x,y)
