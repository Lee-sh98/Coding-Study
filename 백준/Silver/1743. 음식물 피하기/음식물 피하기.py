import sys
input = sys.stdin.readline

def dfs(i, j):
    stack = [(i, j)]
    result = 0

    while stack:
        x, y = stack.pop()
        if not arr[x][y]:
            continue
        result += 1
        arr[x][y] = 0
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if not(0<=nx<N and 0<=ny<M):
                continue
            if arr[nx][ny] == 1:
                stack.append((nx, ny))
    return result
    

N, M, K = map(int, input().split())
arr = [[0]*M for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result = 0

for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

for i in range(N):
    for j in range(M):
        if arr[i][j]==1:
            result = max(result, dfs(i, j))

print(result)
