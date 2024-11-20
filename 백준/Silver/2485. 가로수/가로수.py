import math
N=int(input())
a=[int(input()) for _ in range(N)]
b=[*map(int.__sub__,a[1:],a)]
c=math.gcd(*b)
d=sum(dist//c-1 for dist in b)
print(d)