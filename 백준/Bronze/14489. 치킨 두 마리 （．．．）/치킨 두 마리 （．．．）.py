a,b,c=map(int,open(0).read().split())
print(a+b-2*(a+b>=2*c)*c)