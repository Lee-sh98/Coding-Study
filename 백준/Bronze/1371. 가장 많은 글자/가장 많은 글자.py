a=[0]*26
for c in filter(str.isalpha,open(0).read()):a[ord(c)-97]+=1
print(*[chr(i+97) for i in range(26) if a[i]==max(a)],sep="")