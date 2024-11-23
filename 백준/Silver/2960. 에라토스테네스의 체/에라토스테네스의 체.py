N,K=map(int,input().split())
s=[1]*-~N
for i in range(2,N+1):
 for j in range(i,N+1,i):K-=s[j];s[j]=0;not K and exit(print(j))