import collections as c
i=""
while True:
    try:
        i+=input()
    except:break
a=c.Counter(filter(str.isalpha,i))
b=max(a.values())
print(*sorted(filter(lambda x:a[x]==b,a)),sep="")