import sys
from collections import deque
input = sys.stdin.readline

def dfs(x, y):
    if x==M-1 and y==N-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    result = 0
    for dx, dy in directions:
        nx, ny = x+dx, y+dy

        if not(0<=nx<M and 0<=ny<N):
            continue
        if board[x][y] > board[nx][ny]:
            result += dfs(nx, ny)

    dp[x][y] = result
    return dp[x][y]


M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

print(dfs(0, 0))
