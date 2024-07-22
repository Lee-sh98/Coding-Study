import sys

def tile(n):
    if n==1:
        return 1
    a, b = 1, 2

    for i in range(3, n+1):
        a, b = b%15746, (a+b)%15746
    return b
    
N = int(sys.stdin.readline())

print(tile(N))
