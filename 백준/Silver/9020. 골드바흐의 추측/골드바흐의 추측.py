import sys
input = sys.stdin.readline
MAX = 10_001

def solve(n):
    m = min(filter(lambda i: sieve[i] and sieve[n-i], range(n//2+1)), key= lambda j: (abs(n-2*j), j))
    
    return f"{m} {n-m}"

sieve = [1]*MAX
for i in range(2, int(MAX**0.5)+1):
    cur = i+i
    while cur < MAX:
        sieve[cur] = 0
        cur += i

T = int(input())
for _ in range(T):
    n = int(input())
    print(solve(n))
