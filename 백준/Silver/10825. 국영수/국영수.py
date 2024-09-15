import sys
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N)]
for i in range(N):
    name, *score = input().split()
    arr[i] = [name]+list(map(int, score))

arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for name, *_ in arr:
    print(name)
