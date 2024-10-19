import sys
input = sys.stdin.readline

fact = {}
def factorial(n):
    if n <= 1:
        return 1
    if n not in fact:
        fact[n] = n*factorial(n-1)
    return fact[n]

N = int(input())
commend, *data = map(int, input().split())


if commend == 1:
    k = data[0]
    ans = []
    arr = list(range(1, N+1))

    for i in range(1, N+1):
        f = factorial(N-i)
        s = (k-1)//f
        ans.append(arr.pop(s))
        k -= f*s
    print(*ans)
else:
    data = list(data)
    sort = list(sorted(data))
    ans = 1

    for i in range(1, N+1):
        s = sort.index(data[i-1])
        sort.remove(data[i-1])
        f = factorial(N-i)
        ans += f*s
    print(ans)
