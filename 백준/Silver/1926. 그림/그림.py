import sys
input = sys.stdin.readline

def dfs(x, y):
    result = 0
    stack = [(x, y)]
    
    while stack:
        cx, cy = stack.pop()
        if arr[cx][cy] == 1:
            result += 1
            arr[cx][cy] = 2

        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy

            if 0<=nx<n and 0<=ny<m and arr[nx][ny]==1:
                stack.append((nx, ny))
    return result

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
count = 0
result = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            count += 1
            result = max(result, dfs(i, j))

print(count)
print(result)
