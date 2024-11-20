N,K=map(int,input().split())
q,w,e,r,t=[N],[M:=100001]*M,[0]*M,[K],-1
while(c:=q[t:=t+1])-K:
    for d in(c+1,c-1,2*c):
        if 0<=d<M and w[d]==M:q+=[d];w[d]=c;e[d]=e[c]+1
print(e[K])
while K-N:r+=[K:=w[K]]
print(*r[::-1])