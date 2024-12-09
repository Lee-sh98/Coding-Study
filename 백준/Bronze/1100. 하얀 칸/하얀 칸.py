r=0
for i in range(8):r+=sum(j=='F' for j in input()[i%2::2])
print(r)