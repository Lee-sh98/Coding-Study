(N),(X,S),*t=[map(int,i.split())for i in open(0)]
print(any(p>S for c,p in t if c<=X)*"YES"or"NO")