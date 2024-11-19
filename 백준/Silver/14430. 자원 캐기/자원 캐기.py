N,M=map(int, input().split())
a=[[*map(int, input().split())] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if i==0 and j==0:
            continue
        elif i==0:
            a[i][j]+=a[i][j-1]
        elif j==0:
            a[i][j]+=a[i-1][j]
        else:
            a[i][j]+=max(a[i][j-1],a[i-1][j])

print(a[N-1][M-1])