import sys
input = sys.stdin.readline

def memoize(func):
    memo = {}
    def helper(arr, n):
        if n not in memo:
            memo[n] = func(arr, n)
        return memo[n]
    return helper

def mul(arr, brr):
    result = []
    for a in arr:
        tmp = []
        for b in zip(*brr):
            tmp.append(sum(map(int.__mul__,a,b))%1000)
        result.append(tmp)
    return result

def calc(arr, n):
    if n == 1:
        return arr
    if n == 2:
        return mul(arr, arr)
    else:
        mid = n//2
        return mul(calc(arr, mid), calc(arr, n-mid))

calc = memoize(calc)

N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = calc(arr, B)
for r in result:
    print(*map(lambda x: x%1000, r))
