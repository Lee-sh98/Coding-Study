a=[*open(0)][1][:-1]
b=sum((1,-1)[int(i)%2]for i in a)
print(1 if b<0 else 0 if b>0 else -1)