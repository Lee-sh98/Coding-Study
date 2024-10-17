import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline

def bfs(arr):
    q = deque()
    q.append(arr)

    while q:
        x,y,z = scv = q.popleft()
        if not any(scv):
            return visited[x][y][z]-1

        for per in pers:
            nx, ny, nz = map(lambda s, p: max(s-p, 0), scv, per)
            if not visited[nx][ny][nz]:
                visited[nx][ny][nz] = visited[x][y][z] + 1
                q.append([nx,ny,nz])

N = int(input())
x, y, z = SCV = list(map(int, input().split()))+[0]*(3-N)
visited = [[[0]*61 for _ in range(61)] for _ in range(61)]
visited[x][y][z] = 1
pers = list(permutations([9, 3, 1], 3))

result = bfs(SCV)
print(result)
