a,*b=input()
for c in b:a+=c*(a[-1]!=c)
print(a)