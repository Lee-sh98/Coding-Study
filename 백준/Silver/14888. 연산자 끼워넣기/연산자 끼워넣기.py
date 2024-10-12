import sys
input = sys.stdin.readline

def div(a, b):
    if a>=0:
        return a//b
    else:
        return -(-a//b)

def dfs(acc, idx):
    if idx == N:
        result.append(acc)

    for i in range(4):
        if M[i] > 0:
            M[i] -= 1
            dfs(operator[i](acc, A[idx]), idx+1)
            M[i] += 1

N = int(input())
A = list(map(int, input().split()))
M = list(map(int, input().split()))
operator = [int.__add__, int.__sub__, int.__mul__, div]
result = []
dfs(A[0], 1)

print(max(result))
print(min(result))
