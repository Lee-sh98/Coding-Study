import bisect as f
(N,),a=[[*map(int,i.split())] for i in open(0)]
t=[a[0]]
for b in a[1:]:
    if t[-1]<b:
        t.append(b)
    else:
        t[f.bisect_left(t,b)]=b
print(len(t))