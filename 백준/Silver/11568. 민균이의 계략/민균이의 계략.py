(N,),a=[[*map(int,i.split())] for i in open(0)]
t=[a[0]]
for i,b in enumerate(a[1:]):
    if t[-1]<b:
        t.append(b)
    else:
        for j,c in enumerate(t):
            if c>=b:
                t[j]=b
                break
print(len(t))
