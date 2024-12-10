N=int(input())
a,*s=sorted(map(int,input().split()))
if a==1:
    i=0
    while i<N-1 and a+1==s[i]:
        a=s[i]
        i+=1
    print(a+1)
else:
    print(1)