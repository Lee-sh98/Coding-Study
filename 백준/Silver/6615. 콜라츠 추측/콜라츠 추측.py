import sys
input = sys.stdin.readline

def memoize(func):
    memo = {}

    def helper(n):
        if n not in memo:
            memo[n] = func(n)
        return memo[n]
    return helper

def get_ancestor(n):
    if n == 1:
        return [1]
    if n%2:
        return [n]+get_ancestor(3*n+1)
    else:
        return [n]+get_ancestor(n//2)

get_ancestor = memoize(get_ancestor)

while True:
    A, B = map(int, input().split())
    if A==B==0:
        break

    pA = get_ancestor(A)
    pB = get_ancestor(B)

    common = 0
    for a, b in zip(pA[::-1], pB[::-1]):
        if a==b:
            common += 1
        else:
            break
    SA, SB = len(pA)-common, len(pB)-common
    C = pA[-common]
    print(f"{A} needs {SA} steps, {B} needs {SB} steps, they meet at {C}")
