import sys
input = lambda:int(sys.stdin.readline())
PI = 3.141592

d1 = input()
d2 = input()

print(round(2*(d1+d2*PI), 6))
