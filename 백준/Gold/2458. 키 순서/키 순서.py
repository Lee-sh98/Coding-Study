import sys
input = lambda: map(int, sys.stdin.readline().split())

def dfs(s, c):
    v[c][s] = v[s][c] = 1
    
    for t in e[c]:
        if not v[s][t]:
            dfs(s, t)

N, M = input()
v = [[0]*N for _ in range(N)]
e = [[] for _ in range(N)]

for _ in range(M):
    a, b = input()
    e[a-1].append(b-1)

for i in range(N):
    dfs(i, i)

print(sum(sum(v[i])==N for i in range(N)))
