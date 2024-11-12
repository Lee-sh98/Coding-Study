r=range
n,m=map(int,input().split())
d=[list(map(int,input()))for _ in r(n)]
for i in r(1,n):
    for j in r(1,m):
        if d[i][j]:
            d[i][j]+=min(d[i-1][j],d[i][j-1],d[i-1][j-1])
print(max(map(max,d))**2)