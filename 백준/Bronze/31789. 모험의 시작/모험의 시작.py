(N),(X,S),*t=[map(int,i.split())for i in open(0)]
print("YNEOS"[all(p<=S for c,p in t if c<=X)::2])