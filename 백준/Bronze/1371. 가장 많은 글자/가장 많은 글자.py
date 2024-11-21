a=dict.fromkeys(map(chr,range(97,123)),0)
for c in filter(str.isalpha,open(0).read()):a[c]+=1
print(*filter(lambda x:a[x]==max(a.values()),a),sep="")