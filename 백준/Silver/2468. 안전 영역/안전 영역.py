import sys
input = sys.stdin.readline

def dfs(inspection, i, j):
    stack = [(i, j)]
    inspection[i][j] = 1
    while stack:
        cx, cy = stack.pop()
        
        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy

            if (0<=nx<N and 0<=ny<N) and not inspection[nx][ny]:
                inspection[nx][ny] = 1
                stack.append((nx, ny))

def inspect(height):
    inspection = [[0]*N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            inspection[i][j] = int(arr[i][j]<=height)

    for i in range(N):
        for j in range(N):
            if not inspection[i][j]:
                count += 1
                dfs(inspection, i, j)
    
    return count

N = int(input())
arr= [list(map(int, input().split())) for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

heights = set()
for a in arr:
    for cell in a:
        heights.add(cell)

result = 1
for height in list(heights):
    tmp = inspect(height)
    result = max(result, tmp)
print(result)
