import sys
input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    D = [0]+list(map(int, input().split()))
    children = [[] for _ in range(N+1)]
    indegree = [0]*(N+1)
    dp = [0]*(N+1)

    for _ in range(K):
        X, Y = map(int, input().split())
        children[X].append(Y)
        indegree[Y] += 1

    stack = []
    for i in range(1, N+1):
        if indegree[i] == 0:
            stack.append(i)
            dp[i] = D[i]

    while stack:
        cur = stack.pop()
        
        for child in children[cur]:
            indegree[child] -= 1
            dp[child] = max(dp[child], dp[cur]+D[child])
            if indegree[child] == 0:
                stack.append(child)

    W = int(input())
    print(dp[W])

T = int(input())
for _ in range(T):
    solve()
