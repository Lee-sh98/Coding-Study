N,X,S,*t=map(int,open(0).read().split())
print("YNEOS"[all(p<=S for c,p in zip(t[::2],t[1::2])if c<=X)::2])