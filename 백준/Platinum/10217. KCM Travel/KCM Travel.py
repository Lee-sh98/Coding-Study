import sys
from heapq import *
input = sys.stdin.readline
INF = sys.maxsize

def solve():
    N, M, K = map(int, input().split())
    edges = [[] for _ in range(N+1)]

    for _ in range(K):
        u, v, c, d = map(int, input().split())
        edges[u].append((v, c, d))

    for i in range(N+1):
        edges[i].sort(key=lambda x: (x[2], x[1]))

    dp = [[INF]*(M+1) for _ in range(N+1)]
    dp[1] = [0]*(M+1)

    q = [(0, 0, 1)]
    while q:
        time, cost, cur = heappop(q)

        if cur == N:
            break

        if dp[cur][cost] < time:
            continue
        
        for node, ncost, ntime in edges[cur]:
            nc = cost+ncost
            nt = time+ntime
            
            if nc <= M and nt < dp[node][nc]:
                for c in range(nc, M+1):
                    if nt < dp[node][c]:
                        dp[node][c] = nt
                    else:
                        break
                heappush(q, (nt, nc, node))

    r = dp[N][M]
    print(r if r != INF else "Poor KCM")

T = int(input())
for _ in range(T):
    solve()
