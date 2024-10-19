import sys
sys.setrecursionlimit(10**5)
MOD = 10_007

def binomial(n, k):
    if k==0 or k==n:
        return 1

    if (n,k) not in C:
        C[n, k] = binomial(n-1, k-1)+binomial(n-1, k)
    return C[n, k]

N, K = map(int, sys.stdin.readline().split())

C = {(0, 0):1}

print(binomial(N, K)%MOD)
