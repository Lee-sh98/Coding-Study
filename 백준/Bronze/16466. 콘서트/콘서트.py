N=int(input())
s=[0]+sorted(map(int,input().split()))
i=0
while i<N and s[i]+1==s[i+1]:i+=1
print(s[i]+1)