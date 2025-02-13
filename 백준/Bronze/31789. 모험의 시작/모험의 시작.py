(N),(X,S),*t=[map(int,i.split())for i in open(0)]
print("YNEOS"[max((p for c,p in t if c<=X),default=0)<=S::2])