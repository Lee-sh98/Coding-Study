f=lambda:map(int,input().split())
r=range
def d(s,c):
    v[c][s]=v[s][c]=0
    for t in e[c]:
        if v[s][t]:d(s,t)
N,M=f()
v,e=zip(*[[[1]*N,[]]for _ in r(N)])
for _ in r(M):a,b=f();e[a-1].append(b-1)
for i in r(N):d(i,i)
print(N-sum(map(any,v)))
