import sys
input = sys.stdin.readline

def dfs(cur, depth):
    if depth >= 4:
        return 1

    result = 0
    for node in edges[cur]:

        if not chk[node]:
            chk[node] = True
            result += dfs(node, depth+1)
            chk[node] = False

    return int(result>0)

N, M = map(int, input().split())
edges = [[] for _ in range(N)]
chk = [False]*N
result = 0

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

MAX = 0
for i in range(N):
    chk[i] = True
    MAX+=dfs(i, 0)
    chk[i] = False
    if MAX:
        break

print(int(MAX>0))
