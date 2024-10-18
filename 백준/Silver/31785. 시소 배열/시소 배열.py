import sys
input = sys.stdin.readline
MAX = 500_001

Q = int(input())
i, j = 0, 0
acc = [0]*MAX
result = []

for _ in range(Q):
    commend, *operand = map(int, input().split())
    if commend == 1:
        acc[j+1] = acc[j] + operand[0]
        j += 1
    else:
        half = (i+j)//2
        front, back = acc[half]-acc[i], acc[j]-acc[half]
        result.append(str(min(front, back)))
        
        if front > back:
            j = half
        else:
            i = half

print("\n".join(result))
print(" ".join(map(lambda x: str(acc[x+1]-acc[x]), range(i, j))))
