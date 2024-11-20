import re
_,*a=open(0).read().split()
for b in a:print("YES"if re.fullmatch(r"(100+1+|01)+",b)else"NO")