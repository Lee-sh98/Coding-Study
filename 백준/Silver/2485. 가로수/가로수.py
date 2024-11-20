import math
N,*a=map(int,open(0))
b=[*map(int.__sub__,a[1:],a)]
c=math.gcd(*b)
print(sum(d//c-1 for d in b))