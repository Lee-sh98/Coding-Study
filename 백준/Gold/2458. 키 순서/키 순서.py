f=lambda:map(int,input().split())
def dfs(s,c):
    v[c][s]=v[s][c]=1
    for t in e[c]:
        if not v[s][t]:
            dfs(s, t)
N,M=f()
v=[[0]*N for _ in range(N)]
e=[[]for _ in range(N)]
for _ in range(M):
    a,b=f()
    e[a-1].append(b-1)
for i in range(N):
    dfs(i,i)
print(sum(map(all,v)))
