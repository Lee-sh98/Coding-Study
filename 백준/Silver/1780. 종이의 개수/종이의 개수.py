import sys
from collections import defaultdict
input = sys.stdin.readline

def solution(arr):
    n = len(arr)
    if n==1:
        count[arr[0][0]]+=1
        return
    total = set()

    for line in arr:
        total |= set(line)

    if len(total) == 1:
        count[list(total)[0]] += 1
    else:
        for i in range(0, n, n//3):
            for j in range(0, n, n//3):
                tmp = []
                for k in range(i, i+n//3):
                    tmp.append(arr[k][j:j+n//3])
                solution(tmp)

N = int(input())
count = defaultdict(int)
paper = [list(map(int, input().split())) for _ in range(N)]

solution(paper)

for i in range(-1, 2):
    print(count[i])
