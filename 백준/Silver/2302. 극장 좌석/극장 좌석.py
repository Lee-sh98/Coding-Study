N,M=int(input()),int(input())
f={0:1,1:1}
for i in range(2,42):
    f[i]=f[i-1]+f[i-2]
arr=[int(input()) for _ in range(M)]+[N+1]
l=0
dp=1
for a in arr:
    dp*=f[a-l-1]
    l=a
print(dp)
