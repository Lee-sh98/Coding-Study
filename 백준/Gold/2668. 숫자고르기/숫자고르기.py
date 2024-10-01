import sys
input = sys.stdin.readline

def dfs(x, i):
    visited[x] = True
    y = arr[x]
    if not visited[y]:
        dfs(y, i)
    elif visited[y] and y==i:
        result.append(y)
    

N = int(input())
arr = [0]+[int(input()) for _ in range(N)]
result = []
for i in range(1, N+1):
    visited = [False]*(N+1)
    dfs(i, i)

print(len(result))
for r in sorted(result):
    print(r)
