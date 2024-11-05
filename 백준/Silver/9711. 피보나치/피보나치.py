import sys
input = sys.stdin.readline

T = int(input())
fib = {0:0, 1:1}
for i in range(2, 10_001):
    fib[i] = fib[i-1] + fib[i-2]

for i in range(1, T+1):
    P, Q = map(int, input().split())
    print(f"Case #{i}: {fib[P]%Q}")
