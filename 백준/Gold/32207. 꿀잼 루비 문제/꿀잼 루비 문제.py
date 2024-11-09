import sys
input = sys.stdin.readline

def valid(x, y):
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<M and visited[nx][ny]:
            return False
    return True

def solve(idx, count, value):
    global result
    if count>K:
        return
    result = max(result, value)
    
    for i in range(idx, min(N*M, 36)):
        v, x, y = data[i]
        if valid(x, y):
            visited[x][y] = 1
            solve(i+1, count+1, value+v)
            visited[x][y] = 0

N, M, K = map(int, input().split())
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[0]*M for _ in range(N)]
data = []
result = 0

for i in range(N):
    for j, v in enumerate(map(int, input().split())):
        data.append((v, i, j))

data.sort(reverse=True)
solve(0, 0, 0)
print(result)
