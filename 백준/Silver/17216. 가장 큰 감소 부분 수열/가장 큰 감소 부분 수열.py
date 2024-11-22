N,*A=map(int,open(0).read().split())
d=A[:]
for i in range(1,N):d[i]+=max([d[j]for j in range(i)if A[j]>A[i]]+[0])
print(max(d))