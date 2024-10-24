import sys
input = sys.stdin.readline

n = int(input())
a = list(input().rstrip() for _ in range(n))
a.sort(key=int)
arr = []

for x in a[:4]:
    for y in a[:4]:
        if x!=y:
            arr.append(int(x+y))

arr.sort()
print(arr[2])
