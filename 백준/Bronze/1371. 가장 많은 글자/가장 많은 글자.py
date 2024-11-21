import collections as c,itertools as d
i=[]
while True:
    try:
        i+=[*input()]
    except:break
a=c.Counter(filter(str.isalpha,d.chain(i)))
b=max(a.values())
print(*sorted(filter(lambda x:a[x]==b,a)),sep="")