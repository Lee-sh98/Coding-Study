E,J,F=".JF"
R, C = map(int, input().split())
m = [[*input()]for _ in range(R)]
q,s=[],0
r = "IMPOSSIBLE"
for i in range(R*C):
    j,k=i//C,i%C
    if m[j][k]==J:
        q=[(j,k,1)]+q
    elif m[j][k]==F:
        q+=[(j,k,1)]
while s<len(q):
    x,y,t=q[s];s+=1;w=m[x][y]
    if w==J and(x==0 or x==R-1 or y==0 or y==C-1):r=t;break
    for f,g in zip((x+1,x-1,x,x),(y,y,y+1,y-1)):
        for a,*b in((J,E),(F,J,E)):
            if 0<=f<R and 0<=g<C and w==a and any(map(m[f][g].__eq__,b)):m[f][g]=w;q+=[(f,g,t+1)]
print(r)