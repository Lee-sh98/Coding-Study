N=int(input())
s=[i:=0]+sorted(map(int,input().split()))
while i<N and s[i]+1==s[i+1]:i+=1
print(s[i]+1)