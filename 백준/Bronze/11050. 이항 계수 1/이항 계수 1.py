def binomial(n, k):
    if k<0 or n<k:
        return 0
    if n==k==0:
        return 1
    return binomial(n-1, k-1) + binomial(n-1, k)

def dp(func):
    mem = {}
    def helper(n, k):
        if (n, k) not in mem:
            mem[n, k] = func(n, k)
        return mem[n, k]
    return helper

binomial = dp(binomial)

N, K = map(int, input().split())
print(binomial(N, K))
