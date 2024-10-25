import sys
input = sys.stdin.readline
MAX = 10**100

fib = [1, 2]
while fib[-1] <= MAX:
    fib.append(fib[-1]+fib[-2])

while True:
    a, b = map(int, input().split())
    if a==b==0:
        break
    print(sum(map(lambda f: a<=f<=b, fib)))
