import sys
input = lambda: map(int, sys.stdin.readline().split())

X1, Y1, R1 = input()
X2, Y2, R2 = input()

D = ((X1-X2)**2+(Y1-Y2)**2)**0.5

print(("NO", "YES")[D < R1+R2])
