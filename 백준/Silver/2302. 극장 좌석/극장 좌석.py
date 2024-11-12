N,M,*a=map(int,open(0))
a=[0]+a+[N+1]
d=1
f={0:1,1:1}
for i in range(2,41):f[i]=f[i-1]+f[i-2]
for x,y in zip(a,a[1:]):d*=f[y-x-1]
print(d)