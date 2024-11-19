n,f=int(input()),{0:1,1:1}
for i in range(2,n+1):f[i]=(f[i-1]+f[i-2]+1)%1000000007
print(f[n])