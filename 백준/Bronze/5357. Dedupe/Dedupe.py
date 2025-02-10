r,*s=open(0).read()
for c in s[s.index('\n')+1:]:print(end=c*(r!=c));r=c