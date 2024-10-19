import sys
sys.setrecursionlimit(10**5)

def binomial(n, m):
    if m==0 or m==n:
        return 1

    if (n,m) not in C:
        C[n, m] = binomial(n-1, m-1)+binomial(n-1, m)
    return C[n, m]

C = {(0, 0):1}

print(binomial(*map(int, sys.stdin.readline().split())))
