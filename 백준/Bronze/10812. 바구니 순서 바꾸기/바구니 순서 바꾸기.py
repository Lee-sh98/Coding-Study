(N,M),*a=[[*map(int,i.split())]for i in open(0)]
b=[*range(1,N+1)]
for i,j,k in a:b[i-1:j]=b[k-1:j]+b[i-1:k-1]
print(*b)