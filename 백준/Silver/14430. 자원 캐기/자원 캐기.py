N,M=map(int, input().split())
a=[[0]*(M+1)]+[[0]+[*map(int, input().split())] for _ in range(N)]
for i in range(1,N+1):
    for j in range(1,M+1):
        a[i][j]+=max(a[i][j-1],a[i-1][j])
print(a[N][M])