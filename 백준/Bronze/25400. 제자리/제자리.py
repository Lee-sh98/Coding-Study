N=int(input())
A=[*map(int,input().split())]
count=0
for i in range(N):count+=A[i]!=i+1-count
print(count)