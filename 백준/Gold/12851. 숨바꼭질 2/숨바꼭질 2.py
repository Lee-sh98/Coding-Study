N,K=map(int,input().split())
q,v=[N],[M:=100001]*M;v[N]=r=s=0
while s<len(q):
    c=q[s];s+=1;r+=c==K
    for d in(c+1,c-1,2*c):
        if 0<=d<M and v[c]<v[d]:v[d]=v[c]+1;q+=[d]
print(v[K])
print(r)
