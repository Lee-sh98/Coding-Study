import sys
input = sys.stdin.readline
MAX = 500_001

Q = int(input())
i, j = 0, 0
acc = [0]*MAX

for _ in range(Q):
    commend, *operand = map(int, input().split())
    if commend == 1:
        acc[j+1] = acc[j] + operand[0]
        j += 1
    else:
        half = (i+j)//2
        if acc[half]-acc[i] > acc[j]-acc[half]:
            print(acc[j]-acc[half])
            j = half
        else:
            print(acc[half]-acc[i])
            i = half

for x in range(i, j):
    print(acc[x+1]-acc[x], end=" ")
