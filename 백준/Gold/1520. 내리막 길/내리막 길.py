import sys
input = sys.stdin.readline
sys.setrecursionlimit(250000)

def dfs(x, y):
    if x==M-1 and y==N-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if not(0<=nx<M and 0<=ny<N):
            continue
        if arr[x][y]>arr[nx][ny]:
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dp = [[-1]*N for _ in range(M)]

dfs(0, 0)
print(dp[0][0])
