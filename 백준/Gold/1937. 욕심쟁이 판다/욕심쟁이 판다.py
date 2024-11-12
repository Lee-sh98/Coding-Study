import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y]=1
    for dx, dy in directions:
        nx, ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and graph[x][y]<graph[nx][ny]:
            dp[x][y] = max(dfs(nx, ny)+1, dp[x][y])
    return dp[x][y]

n = int(input())
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
graph = [[*map(int, input().split())] for _ in range(n)]
dp = [[-1]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        dfs(i,j)

print(max(map(max, dp)))
