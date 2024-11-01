import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
MAX = max(arr)
appear = set(arr)
answer = [0]*(MAX+1)

for i in arr:
    if i == MAX:
        continue
    for j in range(2*i, MAX+1, i):
        if j in appear:
            answer[i] += 1
            answer[j] -= 1

print(" ".join(map(lambda x: str(answer[x]) , arr)))
