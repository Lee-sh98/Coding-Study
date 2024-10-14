import sys

MIN, MAX = map(int, sys.stdin.readline().split())
arr = [1]*(MAX-MIN+1)

for i in range(2, int(MAX**0.5)+1):
    sq = i*i
    LOWER = ((MIN-1)//sq+1)*sq
    for j in range(LOWER, MAX+1, sq):
        arr[j-MIN] = 0

print(sum(arr))
