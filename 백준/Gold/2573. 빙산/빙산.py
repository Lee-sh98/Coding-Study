import sys
input = sys.stdin.readline

def check():
    if len(island) == 1:
        return 1
    
    visited = [[False]*M for _ in range(N)]
    count = 0
    for x, y in island:
        if not visited[x][y]:
            count += 1
            stack = [(x, y)]
            while stack:
                cx, cy = stack.pop()
                visited[cx][cy] = True
                for dx, dy in directions:
                    nx, ny = cx+dx, cy+dy
                    if (nx, ny) in island and not visited[nx][ny]:
                        visited[nx][ny] = True
                        stack.append((nx, ny))

    return count

def melt():
    melts = {}

    for x, y in island:
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if arr[nx][ny] == 0:
                melts[x, y] = melts.get((x, y), 0) + 1
    
    for x, y in melts:
        arr[x][y] = max(arr[x][y]-melts[x, y], 0)
        if arr[x][y] == 0:
            island.discard((x, y))             

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0
island = set()

for i in range(N):
    for j in range(M):
        if arr[i][j] > 0:
            island.add((i, j))

while check() == 1:
    melt()
    ans += 1

if check() == 0:
    print(0)
else:
    print(ans)
