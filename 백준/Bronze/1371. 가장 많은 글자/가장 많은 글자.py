a=dict.fromkeys(map(chr,range(97,123)),0)
for c in open(0).read():
    if c.isalpha():a[c]+=1
print(*filter(lambda x:a[x]==max(a.values()),a),sep="")