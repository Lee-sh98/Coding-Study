import sys
from heapq import *
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
dp = [[M*N]*M for _ in range(N)]
dp[0][0] = 0

q = []
heappush(q, (0, 0, 0))
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    dist, cx, cy = heappop(q)
    if cx == N and cy == M:
        continue
    
    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy
        if  0<=nx<N and 0<=ny<M and dp[nx][ny] > dist+graph[nx][ny]:
            dp[nx][ny] = dist+graph[nx][ny]
            q.append((dist+graph[nx][ny], nx, ny))

print(dp[N-1][M-1])
