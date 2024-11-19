(_,N,M),*a=[[0,*map(int,i.split())]for i in open(0)]
a=[[0]*(M+1)]+a
for i in range(1,N+1):
    for j in range(1,M+1):a[i][j]+=max(a[i][j-1],a[i-1][j])
print(a[N][M])