import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
dp = [[0]*N for _ in range(N)]
indegree = [0]*N
outdegree = [0]*N

for _ in range(M):
    a, b = map(int, input().split())
    dp[a-1][b-1] = 1
    indegree[b-1] += 1
    outdegree[a-1] += 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if not dp[i][j] and dp[i][k] and dp[k][j]:
                dp[i][j] = 1
                indegree[j] += 1
                outdegree[i] += 1

print(sum(map(lambda i: indegree[i]+outdegree[i] == N-1, range(N))))
