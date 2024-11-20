N,K=map(int,input().split())
q,w,v,x=[N],[M:=100001]*M,[s:=0]*M,[]
w[N]=N
while s<len(q) and (c:=q[s])!=K:
    c=q[s];s+=1
    for d in(c+1,c-1,2*c):
        if 0<=d<M and w[d]==M:v[d]=v[c]+1;w[d]=c;q+=[d]
print(v[K])
while K!=N:x+=[K];K=w[K]
print(N,*x[::-1])