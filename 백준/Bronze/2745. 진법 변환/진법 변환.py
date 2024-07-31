import sys

N, B = sys.stdin.readline().split()
acc = 1
res = 0

for n in N[::-1]:
    if n.isalpha():
        res += (ord(n)-ord('A')+10)*acc
    else:
        res += int(n)*acc
    acc *= int(B)

print(res)
