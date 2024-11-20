import collections as w
M=100001
N,K=map(int,input().split())
q,v=w.deque([N]),[M]*M;v[N]=r=0
while q:
    c=q.popleft();r+=1*(c==K)
    for d in(c+1,c-1,2*c):
        if 0<=d<M and v[c]<v[d]:v[d]=v[c]+1;q.append(d)
print(v[K])
print(r)