import math
N,*a=map(int,open(0))
b=[*map(int.__sub__,a[1:],a)]
c=math.gcd(*b)
d=sum(dist//c-1 for dist in b)
print(d)