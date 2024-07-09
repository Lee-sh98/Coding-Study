import sys
input = sys.stdin.readline

N = int(input())
factorial = 1
for i in range(1, N+1):
    factorial *= i
s = reversed(str(factorial))

for i, c in enumerate(s):
    if c != "0":
        print(i)
        break
