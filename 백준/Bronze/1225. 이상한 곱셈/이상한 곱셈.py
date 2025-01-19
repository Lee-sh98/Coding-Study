a,b=input().split()
f=lambda s:sum(map(int,s))
print(f(a)*f(b))